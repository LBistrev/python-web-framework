from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from testing_demos.common.validators import only_letters_validator


class Profile(models.Model):
    first_name = models.CharField(
        max_length=25,
        validators=(
            only_letters_validator,
        ),
    )

    last_name = models.CharField(
        max_length=25,
        validators=(
            only_letters_validator,
        ),
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(0),
            MaxValueValidator(140),
        ),
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
