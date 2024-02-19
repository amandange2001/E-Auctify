from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=55)
    type_choices = (
        ("Antiques", "Antiques"),
        ("Electronics", "Electronics"),
        ("Furniture", "Furniture"),
        ("Paintings", "Paintings"),
    )
    category = models.CharField(max_length=50, choices=type_choices, default="")
    desc = models.TextField(max_length=400)
    base_price = models.FloatField()
    image = models.ImageField(upload_to="pics")
    status_choices = (
        ("Upcoming", "Upcoming"),
        ("Active", "Active"),
        ("Closed", "Closed"),
    )
    status = models.CharField(max_length=20, choices=status_choices, default="Active")

    def __str__(self):
        return self.product_name

class Auction(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status_choices = (
        ("Upcoming", "Upcoming"),
        ("Active", "Active"),
        ("Closed", "Closed"),
    )
    status = models.CharField(max_length=20, choices=status_choices, default="Active")

    def __str__(self):
        return self.product.product_name

class Bid(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class ClosedProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, primary_key=True)
    closing_time = models.DateTimeField()
    winner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    final_price = models.FloatField()
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.product.product_name
        
