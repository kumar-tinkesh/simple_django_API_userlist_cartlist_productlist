from django.db import models

# Create your models here.

class RegistrationData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'registration_table'



class product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    discount = models.IntegerField()
    brand = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    rating = models.IntegerField() 

    class Meta:
        db_table = 'product_table'


class cart(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    brand = models.CharField(max_length=20)

    class Meta:
        db_table = 'cart_table'