from django.db import models
from django.utils import timezone

# Create your models here.
class testAppVariety(models.Model):
    APP_TYPE_CHOICE = [
        ('A1', 'APP1'),
        ('A2', 'APP2'),
        ('A3', 'APP3'),
        ('A4', 'APP4'),
        ('A5', 'APP5'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='apps/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=APP_TYPE_CHOICE)
    description = models.TextField(default='')
    
    def __str__(self):
        return self.name
