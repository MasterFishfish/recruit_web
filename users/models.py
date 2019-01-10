from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.db import models
# Create your models here.

class User(AbstractUser):
    pass

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class PotentialUser(models.Model):
    email = models.CharField(
        "联系邮箱",
        max_length=20,
    )
    favoritebrowser = models.CharField(
        "常用浏览器",
        max_length=20,
    )
    job = models.CharField(
        "职业",
        max_length=20,
    )