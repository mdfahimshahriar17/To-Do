from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed')
    ]
    CATEGORY = [
        ('work', 'Work'),
        ('personal', 'Personal'),
        ('other', 'Other')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    due_time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS, default='pending')
    category = models.CharField(max_length=10, choices=CATEGORY)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title