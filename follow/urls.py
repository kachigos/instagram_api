from django.urls import path
from .views import *

urlpatterns = [
    path('', FollowCreateView.as_view(), name='follow')
]