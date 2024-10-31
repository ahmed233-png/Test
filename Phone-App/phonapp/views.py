from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import  JsonResponse
from .forms import CreateNewProduct
from . models import *
from django.contrib import messages
import os
import json
import random
# Create your views here.
def home(request):
    product=MyProduct.objects.all()[0:5]
    return render(request,'phone/index.html',{'product':product})




# Create view to display all product 
def all_products(request):
    products=MyProduct.objects.filter(active=0)
    return render(request,'phone/products.html',{'products':products})




# Create view of detailes 
@login_required(login_url='login')
def product(request,id):
    pro_id=get_object_or_404(MyProduct,pk=id)
    return render(request,'phone/product.html',{'pro_id':pro_id,})





# Create view to add cart
def add_to_cart(request):
       if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            product_status=MyProduct.objects.get(id=product_id)
            if product_status:
                if MyCart.objects.filter(user=request.user.id,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'}, status=200)
                else:
                    if product_status.quantity>=product_qty:
                        MyCart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'}, status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not Available'}, status=200)
            else:
                return JsonResponse({'status':'Login to Add Cart'}, status=200)
        else:
            return JsonResponse({'status':'Invalid Access'}, status=200)
        


# Create view to show cart for customer
def cart(request):
    totel =0
    if request.user.is_authenticated:
        cart = MyCart.objects.filter(user=request.user)
        for sub in cart:
            totel+=sub.product_qty*sub.product.price
    return render(request,'phone/cart.html',{'cart':cart,'totel':totel})



# Create view to delete product from cart
@login_required(login_url='login')
def delete_from_cart(request,id):
    cart = MyCart.objects.get(pk=id)
    cart.delete()
    return render(request,'phone/cart.html')



# Create view to checkout
@login_required(login_url='login')
def checkout(request):
    rowcart=MyCart.objects.filter(user=request.user)
    totel=0
    for item in rowcart:
        totel+=item.product_qty*item.product.price
    return render(request,'phone/check-out.html',{'rowcart':rowcart,'totel':totel,})


# Create view that name is place order
@login_required(login_url='login')
def place_order(request):
    if request.method=='POST':
        neworder=Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pin=request.POST.get('pin')
        neworder.payment_mode=request.POST.get('payment_mode')
        newcart=MyCart.objects.filter(user=request.user)
        totel=0
        for sub in newcart:
            totel+=sub.product_qty*sub.product.price
        neworder.totel_price=totel
        neworder.save()
        newitemorder=MyCart.objects.filter(user=request.user)
        for item in newitemorder:
            OrderItem.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.price,
                quantity=item.product_qty
            )
            orderproduct=MyProduct.objects.filter(id=item.product_id).first()  
            orderproduct.quantity=orderproduct.quantity - item.product_qty
            orderproduct.save()
        MyCart.objects.filter(user=request.user).delete()   
    return redirect('home')



# Create view that cal totel for pay razor
@login_required(login_url='login')
def pay_razor(request):
    cart=MyCart.objects.filter(user=request.user)
    totel=0
    for item in cart:
        totel+=item.product.price*item.product_qty
    return JsonResponse(
        {
            'totel':totel,
        }
    )