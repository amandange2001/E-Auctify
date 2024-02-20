from django.contrib import admin
from .models import Product, Bid, ClosedProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "product_id",
        "product_name",
        "category",
        "desc",
        "base_price",
        "image",
        "status",
        "starttime",
        "duration",
    ]


class BidAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "user",
        "amount",
        "timestamp",
    ]

class ClosedProductAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "closing_time",
        "winner",
        "final_price",
        "is_sold",
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(ClosedProduct, ClosedProductAdmin)
