from django.contrib import admin
from .models import ( Customer , Product , Cart , OrderPlaced )


# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'Customer'
    list_display = ['id','user','name','locality','city','zipcode','state']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'Product'
    list_display = ['id', 'title','selling_price','discount_price','description','brand','category','product_image']
   

@admin.register(Cart)
class CardModelAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'Cart'
    list_display = ['id','user','product','qty']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    can_delete = False
    verbose_name_plural = 'OrderPlaced'
    list_display = ['id','user','customer','product','qty','ordered_date','status']

