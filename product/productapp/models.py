from django.db import models

# Create your models here.

class product(models.Model):
    productname=models.CharField(max_length=10)
    productId= models.IntegerField()

    def __str__(self):
        return self.productname

