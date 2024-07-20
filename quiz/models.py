from django.db import models
from datetime import date

class Results(models.Model):
    category = models.CharField(max_length=255)
    questions_attempted = models.CharField(max_length=255)
    percentage_score = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default=f'Anonymous{date.today()}')


    def __str__(self):
        return self.name

