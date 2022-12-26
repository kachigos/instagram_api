from django.db import models
from django.contrib.auth import get_user_model
from post.models import Profile

User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(Profile, related_name='follow', on_delete=models.CASCADE)

    def __str__(self):
        return self.user