# Generated by Django 4.0.6 on 2022-07-21 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_rename_if_staff_appuser_is_staff'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('first_name', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
