from django.urls import path
from .views import *

urlpatterns = [
    path('add_post/',AddPost.as_view(), name='addPost'),
    path('post/edit/<slug:slug>',UpdatePost.as_view(), name='updatePost'),
    path('post/<slug:slug>/delete', DeletePost.as_view(), name='deletePost'),
    path('',PostList.as_view(), name = 'home'),
    # path('<slug:slug>/',PostDetail.as_view(), name='postDetail'),
    path('post/<slug:slug>/',post_detail, name='postDetail'),
]