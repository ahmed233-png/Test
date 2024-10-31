from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyProduct(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.IntegerField()
    photo=models.ImageField(upload_to='pic')
    active=models.BooleanField(default=False)
    create_by=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    create_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return   '   Name Of Product  : '   +  self.name  +   ' The   Id   Is :  ' +  str(self.id)
    class Meta:
        ordering=['-create_date']


class MyCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(MyProduct,on_delete=models.CASCADE,null=True,blank=True)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        
        total = self.product_qty*self.product.price 
        return total

    def __str__(self):
        return '  Cart Name Is: '  +  self.user.username
    

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    address=models.TextField(max_length=255)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    country=models.CharField(max_length=150)
    pin=models.CharField(max_length=150)
    totel_price=models.DecimalField(max_digits=6,decimal_places=2)
    payment_mode=models.CharField(max_length=150)
    payment_id=models.CharField(max_length=150,null=True)
    message=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)



class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,null=True,blank=True)
    product=models.ForeignKey(MyProduct,on_delete=models.CASCADE,null=True,blank=True)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
   
