from django.db import models


class Search(models.Model):

    name = models.CharField(max_length=1000)
    result = models.CharField(max_length=1000)
    media = models.CharField(max_length=1000)
    media_result = models.CharField(max_length=1000)

    def __str__(self):
        return self.question_text
