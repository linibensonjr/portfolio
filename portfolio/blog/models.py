from pyexpat import model
from django.db import models
from datetime import datetime
from django.utils import timezone


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    episode = models.IntegerField()
    date_pub = models.DateField(default=timezone.now)
    post = models.TextField()

    def publish(self):
        self.date_pub = timezone.now()
        self.save()

    def __str__(self):
        return self.title