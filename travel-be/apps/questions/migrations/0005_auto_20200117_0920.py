# Generated by Django 2.0 on 2020-01-17 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('questions', '0004_auto_20200117_0852'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionCategorys',
            new_name='QuestionCategories',
        ),
    ]