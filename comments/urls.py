from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CommentViewSet, toggle_like

router = DefaultRouter()

router.register('', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('toggle_like/<int:p_id>/', toggle_like),
]
