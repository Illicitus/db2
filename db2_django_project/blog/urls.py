from django.urls import path
from blog.views import Home, Like, ArticleDetail, ArticleDetailLike

app_name = 'blog'

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('like/<int:post>/', Like.as_view(), name='like'),
    path('article_detail_like/<int:post>/', ArticleDetailLike.as_view(), name='article_detail_like'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),

]
