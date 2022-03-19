from django.contrib import admin

# Register your models here.
from  .models import Shop, Menu, Order, Orderfood 

admin.site.register(Shop)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(Orderfood)
