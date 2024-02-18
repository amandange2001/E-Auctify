from django.contrib import admin
from .models import Product, Auction, Bid, ClosedProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "product_id",
        "product_name",
        "category",
        "desc",
        "base_price",
        "image",
    ]

class AuctionAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "start_time",
        "end_time",
        "status",
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
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(ClosedProduct, ClosedProductAdmin)
