# Generated by Django 4.1.7 on 2023-03-02 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_remove_question_daily_subm_limit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 3, 2, 11, 28, 51, 390129, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 3, 2, 11, 28, 58, 378151, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
