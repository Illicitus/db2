from django.core.management.base import BaseCommand

from accounts.models import User
from blog.models import Article

from utils import generate_random_data


class Command(BaseCommand):
    help = 'Create articles'
    author = User.objects.all().order_by('id').last()
    article = Article.objects.all().order_by('id').last()

    def handle(self, *args, **options):

        # Create author model
        try:
            author_id = 1 + self.author.id
        except AttributeError:
            author_id = 1

        username = 'user' + str(author_id)

        author = User.objects.create(
            id=author_id,
            username='{0}'.format(username),
            email='{0}@gmail.com'.format(username),
        )
        author.set_password('password')
        author.save()

        # Create article models
        try:
            article_id = 1 + self.article.id
        except AttributeError:
            article_id = 1

        for unit in range(20):
            article = Article.objects.create(
                title='{0}'.format('news' + str(article_id)),
                body=generate_random_data(length=6, type='string'),
                author=author,
            )
            article.liked_by.add(author)

            article_id += 1

        # Success message for result visualisation in command line and for tests
        self.stdout.write(self.style.SUCCESS('Successfully created 20 posts.'))
