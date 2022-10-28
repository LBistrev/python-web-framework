from django.urls import path

from .views import create_fake_user

urlpatterns = (
    path('fake-user/', create_fake_user, name='fake user'),
)

from .signals import *
