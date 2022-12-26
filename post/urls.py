from django.urls import path
from .views import *

urlpatterns = [
    path("<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("", PostListView.as_view(), name="post_list"),
    path("create_post/", PostCreateView.as_view(), name="post_create"),
    path("create_profile/", ProfileCreateView.as_view(), name="profile_create"),
    path("users/", ProfileListView.as_view(), name="users"),
    path('post_like/<int:p_id>/', toggle_like),
]