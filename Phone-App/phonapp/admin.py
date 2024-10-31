from django.contrib import admin
from .models import MyProduct,MyCart,Order,OrderItem
# Register your models here.
class AhmedPhone(admin.ModelAdmin):
    admin.site.site_header='E-commer'
    admin.site.site_title='Ahome-Store'
admin.site.register(MyProduct,AhmedPhone)
admin.site.register(MyCart)
admin.site.register(Order)
admin.site.register(OrderItem)
