# Generated by Django 2.0 on 2017-12-20 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='liked_by',
            field=models.ManyToManyField(blank=True, null=True, related_name='article_liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]