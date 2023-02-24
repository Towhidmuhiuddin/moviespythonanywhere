from django.contrib import admin
from .models import Category,Movie,Ticket,Wishlist,Order,OrderItem,Profile

# Register your models here.
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Wishlist)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Profile)
