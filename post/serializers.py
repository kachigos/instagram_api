from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post, Profile, Like
from comments.serializers import *
from follow.serializers import FollowSerializer

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance: Post):
        rep = super().to_representation(instance)
        rep["comments"] = CommentSerializer(instance.comments.all(), many=True).data
        rep["likes"] = instance.post_likes.all().count()
        rep["liked_by_user"] = False


        request = self.context.get("request")

        if request.user.is_authenticated:
            rep["liked_by_user"] = Like.objects.filter(user=request.user, product=instance).exists()


        return rep

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

    def to_representation(self, instance: Post):
        rep = super().to_representation(instance)
        rep["followers"] = FollowSerializer(instance.follow.all(), many=True).data
        rep["count"] = instance.follow.all().count()

        return rep