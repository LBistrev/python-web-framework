from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models

from auth_demos.auth_app.managers import AppUsersManager


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 25

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )


'''
    1. Create a model extending AbstractBaseUser and PermissionsMixin
    2. Tell Django for your user model:
    - AUTH_USER_MODEL = 'app_name.model_name' in settings.py (in our case: 'auth_app.AppUser') 
    3. Create user manager
'''

# UserModel = get_user_model()
#
#
# class UserWithFullNameProxy(UserModel):
#     # we can't add new columns but all for functionality
#     @property
#     def full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#
# # User with Profile
# class Profile(models.Model):
#     # fields
#     # profile_image
#     # date_of_birth
#
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#
#
# # Only user Model extending the base
# class CustomUser:
#     # fields
#     # profile_image
#     # date_of_birth
#
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#
#
# # Almost Completely custom user model
# class AppUser:
#     pass
#     # email
#     # password
#     # is_staff
#     # is_superuser
#
#
# class Profile:
#     # first_name
#     # last_name
#     # profile_image
#     user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
