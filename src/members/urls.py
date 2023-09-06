from django.urls import path, include
from .views import UserRegistration

urlpatterns = [
    path('signUp/', UserRegistration.as_view(), name='signUp'),
]
