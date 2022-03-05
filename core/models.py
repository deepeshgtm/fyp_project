from django.db import models


# Create your models here.
class Doctor(models.Model):
    NMC_no = models.CharField(max_length=10, unique=True)
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Contact_no = models.CharField(max_length=20, unique=True)
    Email = models.CharField(max_length=40, null=True, blank=True)
    Address =models.CharField(max_length=40)
    Hospital_worked_at = models.CharField(max_length=30)
    Specialist = models.CharField(max_length=30)

    def __str__(self):
        return self.First_name

class Users(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    Contact_no = models.CharField(max_length=20)
    Email = models.CharField(max_length=40)
    Address = models.CharField(max_length=40)
    Blood_group = models.CharField(max_length=20)

    def __str__(self):
        return self.First_name

