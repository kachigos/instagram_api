from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from account.send_email import send_notification


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    img = models.ImageField(upload_to='profile_img', blank=True, null=True)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'profile'
        verbose_name_plural = 'profile'

class Post(models.Model):
    profile = models.ForeignKey(Profile,related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_img', blank=True, null=True)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.profile)

class Like(models.Model):
    user = models.ForeignKey(User, related_name='post_likes', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='post_likes', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


@receiver(post_save, sender=Post)
def new_post(instance, *args, **kwargs):
    send_notification(instance.id)

