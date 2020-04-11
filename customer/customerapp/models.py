from django.db import models

# Create your models here.

class customer(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    customerId= models.IntegerField()

    def __str__(self):
        return self.firstname

