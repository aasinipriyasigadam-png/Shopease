from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(max_length=10)
    image=models.CharField(max_length=500)
    description=models.CharField(max_length=500)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product_id=models.ForeignKey(Products,on_delete = models.DO_NOTHING)
    count=models.IntegerField(default=1)

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    product_id=models.ForeignKey(Products,on_delete=models.DO_NOTHING)
    order_date=models.DateTimeField(auto_now=True)




