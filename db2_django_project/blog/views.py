from django.views import View
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from blog.models import Article, Comment
from blog.forms import SearchForm, CommentForm

from utils import gen_page_list
from decorators import class_view_decorator


@class_view_decorator(login_required)
class Home(View):
    """
    Return the home page with post list.
    """
    form_class = SearchForm
    template_name = 'home.html'

    def get(self, request):
        form = self.form_class(request.GET)

        if form.is_valid():
            data = form.cleaned_data
            keyword = data.get('search_text', '')

            if data.get('sort_by'):
                post_list = Article.objects.filter(Q(title__contains=keyword) | Q(body__contains=keyword)).order_by(
                    'author__' + data.get('sort_by'))
            else:
                post_list = Article.objects.filter(Q(title__contains=keyword) | Q(body__contains=keyword))

        else:
            form = SearchForm()
            post_list = Article.objects.all()

        # Pagination part
        page = request.GET.get('page', 1)
        paginator = Paginator(post_list, 6)

        try:
            page_come = paginator.page(page)
        except PageNotAnInteger:
            page_come = paginator.page(1)
        except EmptyPage:
            page_come = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {
            'form': form,
            'post_list': page_come,
            'pagination': gen_page_list(page, paginator.num_pages)
        })


@class_view_decorator(login_required)
class Like(View):
    """
    Add or remove like for post, from current user.
    """

    def get(self, request, post):
        article = get_object_or_404(Article, id=post)

        if request.user not in article.liked_by.all():
            article.liked_by.add(request.user)
        else:
            article.liked_by.remove(request.user)
        article.save()

        return redirect('blog:home')


@class_view_decorator(login_required)
class ArticleDetail(View):
    """
    pass
    """
    template_name = 'article_detail.html'
    form_class = CommentForm

    def get(self, request, pk):
        form = self.form_class()
        article = get_object_or_404(Article, pk=pk)
        comments = article.comment.all()

        # Pagination part
        page = request.GET.get('page', 1)
        paginator = Paginator(comments, 6)

        try:
            page_come = paginator.page(page)
        except PageNotAnInteger:
            page_come = paginator.page(1)
        except EmptyPage:
            page_come = paginator.page(paginator.num_pages)
        return render(request, self.template_name, {
            'form': form,
            'article': article,
            'comments': page_come,
            'pagination': gen_page_list(page, paginator.num_pages)
        })

    def post(self, request, pk):
        form = self.form_class(request.POST)
        article = get_object_or_404(Article, pk=pk)

        if form.is_valid():
            data = form.cleaned_data

            comment = Comment.objects.create(
                author=request.user,
                body=data.get('body')
            )
            comment.article_comment.add(article)
            comment.save()

            return redirect('blog:article_detail', pk=pk)

        else:
            return render(request, self.template_name, {'form': form,
                                                        'article': article})


@class_view_decorator(login_required)
class ArticleDetailLike(View):
    """
    Add or remove like for post, from current user and redirect to current article detail page.
    """

    def get(self, request, post):
        article = get_object_or_404(Article, id=post)

        if request.user not in article.liked_by.all():
            article.liked_by.add(request.user)
        else:
            article.liked_by.remove(request.user)
        article.save()

        return redirect('blog:article_detail', pk=post)
