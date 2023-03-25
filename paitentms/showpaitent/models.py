from django.db import models

# Create your models here.
class Paitent(models.Model):
    uname=models.CharField(max_length=100)
    uid=models.IntegerField()
    Dob=models.DateField()
