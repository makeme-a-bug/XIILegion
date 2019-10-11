from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings
from django.urls import reverse
from users.models import roles
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    user_img=models.FileField(default=None,null=True)
    forum_name=models.CharField(max_length=200 , default='')
    Discord_name=models.CharField(max_length=200 , default='')
    role=models.ForeignKey(roles , null=True , on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class Thread_category(models.Model):
    category_title=models.CharField(max_length=200,default=None)
    time_created=models.DateTimeField(default=timezone.now)
    description=models.CharField(max_length=200,blank=True,null=True,default='o')
    author= models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.category_title
    def get_absolute_url(self):
        return reverse('account:forums')

class Thread(models.Model):
    category=models.ForeignKey(Thread_category,on_delete=models.CASCADE)
    queston = models.CharField(max_length=200 , default = None)
    detail = models.TextField()
    author= models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    time_created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.category
    def get_absolute_url(self):
        return reverse('account:forums')

class thread_reply(models.Model):
    thread = models.ForeignKey(Thread,on_delete=models.CASCADE)
    reply = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    time_created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.thread.queston+'__'+self.author.username

class games(models.Model):
    game_title=models.CharField(max_length=200 , default=None)
    game_description=models.TextField()
    game_image=models.FileField()
    author=models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    time_created=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.game_title
    def get_absolute_url(self):
        return reverse('account:home')

class Posts(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    title = models.CharField(max_length=200,default=None)
    body = models.TextField()
    post_img = models.FileField()
    time_created=models.DateTimeField(default=timezone.now)
    category=models.ForeignKey(games,on_delete=models.SET_NULL, null=True , default=None)
    def __str__(self):
        return self.title+'__'+self.author.username
    def get_absolute_url(self):
        return reverse('account:detail',kwargs={'pk': self.pk})


class post_reply(models.Model):
    author= models.ForeignKey(User,on_delete=models.SET_NULL , null=True)
    reply = models.TextField()
    time_created=models.DateTimeField(default=timezone.now)
    post=models.ForeignKey(Posts,on_delete=models.CASCADE)
