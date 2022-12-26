from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from .models import Like
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CommentViewSet(mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

@api_view(["GET"])
def toggle_like(request, p_id):
    user = request.user
    comments = get_object_or_404(Comment, id=p_id)

    if Like.objects.filter(user=user, comments=comments).exists():
        Like.objects.filter(user=user, comments=comments).delete()
    else:
        Like.objects.create(user=user, comments=comments)
    return Response("Like toggled", 200)