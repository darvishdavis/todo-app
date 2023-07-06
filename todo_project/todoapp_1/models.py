from django.db import models

# Create your models here.


class TodoDetails(models.Model):
    task = models.TextField()
    priority = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return self.task