from django.db import models

# Create your models here.
class AddItems(models.Model):
    Purpose = models.CharField(max_length=120)
    Amount = models.IntegerField()
    Reason = models.CharField(max_length=500) 

    def __str__(self):
        return self.Purpose