# Generated by Django 4.1.7 on 2023-02-19 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]