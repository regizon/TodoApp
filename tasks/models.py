from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    status_variations = [
        ("N", "New"),
        ("D", "Done")
    ]
    priority_variations = [
        ('1', 'High'),
        ('2', 'Medium'),
        ('3', 'Low')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=status_variations, default="N")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.CharField(max_length=1, choices=priority_variations, default="1")