from django.db import models
from datetime import datetime

class ToDo(models.Model):

    STATUS_CHOICES = (
        ('A', 'A fazer'),
        ('F', 'Fazendo'),
        ('P', 'Pronto')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(default=datetime.today)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False, default='A')
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title