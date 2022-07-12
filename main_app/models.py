from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Event(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    timeBeg = models.TimeField(auto_now=False, auto_now_add=False)
    timeEnd = models.TimeField(auto_now=False, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('dashboard')

    class Meta:
        ordering = ['timeBeg']


class Date(models.Model):
    date = models.DateField()
