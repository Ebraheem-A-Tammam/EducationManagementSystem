from math import ceil
from datetime import date

from django.utils.text import slugify
from django.db import models
from django.urls import reverse


class Quiz(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField()
    category = models.ForeignKey(
            'Category',
            on_delete = models.CASCADE,
            related_name = 'quizzes',
    )
    difficulty = models.CharField(max_length=100)
    duration = models.DurationField()
    tags = models.ManyToManyField('Tag')
    questions = models.ManyToManyField('Question')
    daily_subm_limit = models.IntegerField(default=2)

    def __str__(self):
        return self.title 

    def get_absolute_url(self):
        return reverse('quizzes:quiz_detail',kwargs={'slug':self.slug})

    def score_to_pass(self):
        return ceil((len(self.questions.all()) * 70.0) / 100.0)

    def daily_subm_limit_exceeded(self, user):
        return self.submissions.filter(user=user, start_time__date=date.today()).count() >= self.daily_subm_limit

def quiz_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

models.signals.pre_save.connect(quiz_pre_save, sender=Quiz)


class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag
