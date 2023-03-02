import uuid

from django.utils import timezone as tz
from django.db import models

from accounts.models import CustomUser


class Submission(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    quiz = models.ForeignKey(
        'Quiz',
        on_delete=models.CASCADE,
        related_name='submissions',
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='submissions',
    )
    start_time = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)


    def __str__(self):
        return f'{str(self.user)} | {str(self.quiz)} | {self.start_time}'

    def get_total_score(self):
        score = 0
        for a in self.items.all():
            if a.question.true_answer == a.answer:
                score += 1
        return score

    def passed(self):
        scored = self.get_total_score()
        return scored >= self.quiz.score_to_pass()

    def end_time(self):
        return self.start_time + self.quiz.duration

    def ended(self):
        return tz.now() > self.end_time()



class AnswerItem(models.Model):
    submission = models.ForeignKey(
        Submission,
        on_delete=models.CASCADE,
        related_name='items',
    )
    question = models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )
    answer = models.ForeignKey(
        'Answer',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{str(self.question)} : {str(self.answer)}'