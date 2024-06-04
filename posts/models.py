from django.db import models

# Create your models here.
class Enquiry(models.Model):
    Name = models.CharField(max_length=75)
    Level = models.CharField(max_length=10)
    Course = models.CharField(max_length=30)
    Preferred_Timing = models.CharField(max_length=30)
    Contact = models.CharField(max_length=30, default='SOME STRING')

    
    def __str__(self):
        return self.title
    

