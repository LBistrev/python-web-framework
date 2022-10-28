from celery import shared_task
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@shared_task
def send_successful_registration_email(user_pk):
    user = UserModel.objects.get(pk=user_pk)
