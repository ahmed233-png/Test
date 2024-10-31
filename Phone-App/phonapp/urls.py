from django.urls import *
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('All/Products/Page',views.all_products,name='all'),
    path('Product/Page/<int:id>',views.product,name='show'),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('Cart/Page',views.cart,name='cart'),
    path('Check-out/Page',views.checkout,name='check-out'),
    path('Delete/From/Cart/<int:id>',views.delete_from_cart,name='remove'),
    path('Place/Order/Page',views.place_order,name='placeorder'),
    path('to-pay',views.pay_razor,),
]
