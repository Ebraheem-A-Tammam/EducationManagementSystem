from django.db import models
from django.urls import reverse


class Question(models.Model):
    question = models.TextField()
    answers = models.ManyToManyField('Answer')
    true_answer = models.ForeignKey(
            'Answer',
            on_delete = models.CASCADE,
            related_name = 'true_for',
    )
    q_type = models.CharField(max_length=50) # denote something like contain matrices or not

    def __str__(self):
        return self.question
    
    def get_absolute_url(self):
        return reverse("quizzes:question_detail",kwargs={'question_id':self.id})


class Answer(models.Model):
    answer = models.TextField()

    def __str__(self):
        return self.answer