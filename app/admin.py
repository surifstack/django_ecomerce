from django.contrib import admin
from app.models import ( Customer , Product , Cart , OrderPlaced )


# Register your models here.

admin.site.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
   
    list_display = ['id','user','name','locality','city','zipcode','state']

admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
   
    list_display = ['id', 'title','selling_price','discount_price','description','brand','category','product_image']
   

admin.site.register(Cart)
class CardModelAdmin(admin.ModelAdmin):
   
    list_display = ['id','user','product','qty']

admin.site.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    
    list_display = ['id','user','customer','product','qty','ordered_date','status']

