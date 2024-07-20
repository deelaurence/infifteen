from django.db import models
from datetime import date

class Results(models.Model):
    category = models.CharField()
    questions_attempted = models.CharField()
    percentage_score = models.CharField()
    name = models.CharField(default=f'Anonymous{date.today()}')


    def __str__(self):
        return self.name

