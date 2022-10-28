import random

from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render

UserModel = get_user_model()


def create_fake_user(request):
    rand_count = 7
    username_suffix = ''.join(str(random.randint(1, 1000)) for _ in range(rand_count))
    UserModel.objects.create_user(
        username=f'lyubo-{username_suffix}',
        password='1lyubo#2323@!)bistrev-$!',
        email='',
    )
    return HttpResponse('It works')
