# Generated by Django 3.0 on 2019-12-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20191219_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='interest',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]
