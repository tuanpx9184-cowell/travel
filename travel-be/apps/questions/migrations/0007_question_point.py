# Generated by Django 2.0 on 2020-01-19 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20200117_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='point',
            field=models.IntegerField(default=0),
        ),
    ]