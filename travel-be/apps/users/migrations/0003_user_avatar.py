# Generated by Django 2.0 on 2019-12-29 08:05

import apps.users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191224_0825'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=apps.users.models.avatar_path),
        ),
    ]