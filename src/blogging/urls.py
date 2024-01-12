from django.urls import path, include
from .views import *
from rest_framework.routers import SimpleRouter
from .apiViews import UserViewset, PostViewset, CategoryViewset
from drf_yasg import openapi
from drf_yasg.views import get_schema_view 
from rest_framework import permissions

# for open api schema
schema_view = get_schema_view(
    openapi.Info(
        title="Blogging API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="raman.c@applify.co"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = SimpleRouter()
router.register('api/v1/users', UserViewset, basename='users')
router.register('api/v1/posts', PostViewset, basename='posts')
router.register('api/v1/category', CategoryViewset, basename='category')

urlpatterns = [
    path('add_post/',AddPost.as_view(), name='addPost'),
    path('post/edit/<slug:slug>',UpdatePost.as_view(), name='updatePost'),
    path('post/<slug:slug>/delete', DeletePost.as_view(), name='deletePost'),
    path('',PostList.as_view(), name = 'home'),
    # path('<slug:slug>/',PostDetail.as_view(), name='postDetail'),
    path('post/<slug:slug>/',post_detail, name='postDetail'),
    path('category/<str:cats>/', categoryView, name='category'),
    path('api/auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
] + router.urls