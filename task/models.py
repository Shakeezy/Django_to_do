from django.db import models
from autentification.models import CustomUser

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False, null=False)
    done = models.BooleanField(default=False)
    def __str__(self):
        return self.title
