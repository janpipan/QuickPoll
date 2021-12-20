from django.db import models
from django.urls import reverse

class Poll(models.Model):
    question = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    multiple_answers = models.BooleanField(default=False)
    add_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('home')


class Answer(models.Model):
    question_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.answer
