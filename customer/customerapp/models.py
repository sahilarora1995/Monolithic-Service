from django.db import models
from django_mysql.models import ListCharField
from django.db.models import CharField, Model

# Create your models here.

class customer(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    customerId= models.IntegerField()
    cart=  ListCharField(
        base_field=CharField(max_length=10),
        size=6,
        max_length=(6 * 11)  # 6 * 10 character nominals, plus commas
    )

    def __str__(self):
        return self.firstname

