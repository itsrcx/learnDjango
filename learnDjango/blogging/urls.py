from django.urls import path
from .views import *

urlpatterns = [
    path('',PostList.as_view(), name = 'home'),
    path('<slug:slug>/',PostDetail.as_view(), name='postDetail'),
]