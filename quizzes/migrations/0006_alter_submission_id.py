# Generated by Django 4.1.6 on 2023-02-15 11:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0005_delete_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]