from django.contrib import admin
from .models import Product, UpcomingProduct, ClosedProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "userid",
        "product_id",
        "product_name",
        "category",
        "desc",
        "base_price",
        "image",
        "time",
    ]

class UpcomingProductAdmin(admin.ModelAdmin):
    list_display = [
        "product",
        "start_time",
        "end_time",
        "status",
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
admin.site.register(UpcomingProduct, UpcomingProductAdmin)
admin.site.register(ClosedProduct, ClosedProductAdmin)