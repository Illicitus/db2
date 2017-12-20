from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver


class User(AbstractUser):
    """
    Create basic user with next custom fields:
    birthday, country, city.
    """
    username = models.CharField(max_length=150)
    email = models.EmailField(max_length=200, unique=True)
    email_confirmed = models.BooleanField(default=False)

    birthday = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


# @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         User.objects.create(user=instance)
    #     instance.user.save()
