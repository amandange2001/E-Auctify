from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=55)
    type = (("Antiques", "Antiques"), ("Electronics", "Electronics"), ("Furnitures", "Furnitures"), ("Paintings", "Paintings"))
    category = models.CharField(max_length=50, choices=type, default="")
    desc = models.TextField(max_length=100)
    base_price = models.FloatField()
    image = models.ImageField(upload_to="pics")
    time = models.TimeField()
    objects = models.Manager()

class UpcomingProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default="Upcoming")  # Upcoming, Open, Closed

class ClosedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    closing_time = models.DateTimeField()
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    final_price = models.FloatField()
    is_sold = models.BooleanField(default=False)