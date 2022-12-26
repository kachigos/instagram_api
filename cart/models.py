from django.db import models
from django.contrib.auth import get_user_model
from post.models import Post


User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Post, related_name='products', on_delete=models.CASCADE)
    count = models.IntegerField()



