from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
# one to many -> Foreign key
class testAppReview(models.Model):
    app = models.ForeignKey(testAppVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.app.name}'

# related name -> what is my name in other table

# many to many
class store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    app_varities = models.ManyToManyField(testAppVariety, related_name='stores')

    def __str__(self):
        return self.name 


# one to one
class testAppCertificate(models.Model):
    app = models.OneToOneField(testAppVariety, on_delete=models.CASCADE, related_name='certificate') 
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.name.app}'
