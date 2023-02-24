from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,date



import os

def get_file_path(request,filename):
    original_filename = filename
    nowTime=datetime.now().strftime('%Y%M%D%H:%M:%S')
    filename="%s%s" % (nowTime,original_filename)
    return os.path.join('uploads/',filename)
# Create your models here.
class Category(models.Model):
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description=models.TextField(max_length=500,null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=hidden")
    release=models.BooleanField(default=False,help_text="0=default,1=Release")
    created_at=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.name
    
class Movie(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=150,null=False,blank=False)
    movie_image=models.ImageField(upload_to=get_file_path,null=True,blank=True)
    producer=models.CharField(max_length=150,null=False,blank=False)
    actor=models.CharField(max_length=500, null=False, blank=False)
    small_description=models.CharField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    description=models.TextField(max_length=500,null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    scedule_date=models.DateField(auto_now=False, auto_now_add=False,blank=True)
    status=models.BooleanField(default=False,help_text="0=default,1=hidden")
    release=models.BooleanField(default=False,help_text="0=default,1=Release")
    tag=models.CharField(max_length=150,null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    ticket_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateField(auto_now_add=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)  
    created_at =models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150, null=False)      
    lname = models.CharField(max_length=150, null=False)      
    email = models.CharField(max_length=150, null=False)      
    phone = models.CharField(max_length=150, null=False)      
    address = models.TextField(null=False)     
    city = models.CharField(max_length=150, null=False)      
    state = models.CharField(max_length=150, null=False)      
    country = models.CharField(max_length=150, null=False)      
    pincode = models.CharField(max_length=150, null=False)

    total_price = models.FloatField(null=False)      
    payment_mode = models.CharField(max_length=150, null=False)      
    payment_id = models.CharField(max_length=250, null=True) 
    
    orderstatuses = (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status = models.CharField(max_length=150, choices=orderstatuses,default='Pending') 
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150, null=True)
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return '{}-{}'.format(self.id,self.tracking_no)

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE) 
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{}-{}'.format(self.order.id,self.order.tracking_no) 

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) 
    phone =models.CharField(max_length=50, null=False)
    address = models.TextField(null=False)     
    city = models.CharField(max_length=150, null=False)      
    state = models.CharField(max_length=150, null=False)      
    country = models.CharField(max_length=150, null=False)      
    pincode = models.CharField(max_length=150, null=False)  
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username       

    