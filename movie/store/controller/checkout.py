from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from store.models import Movie, Ticket,Order,OrderItem,Profile
import random

@login_required(login_url='loginpage')  
def index(request):
    rawticket = Ticket.objects.filter(user=request.user)
    for item in rawticket:
        if item.ticket_qty>item.movie.quantity:
            Ticket.objects.delete(id=item.id)

    ticketitems = Ticket.objects.filter(user=request.user)
    total_price=0

    for item in ticketitems:
        total_price=total_price+item.movie.selling_price*item.ticket_qty

    context ={'ticketitems':ticketitems,'total_price':total_price}
    return render(request,'store/checkout.html', context)



@login_required(login_url='loginpage')  
def ticketorder(request):
    if request.method == 'POST':
        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name:
            currentuser.first_name=request.POST.get('fname')
            currentuser.last_name=request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.phone=request.POST.get('phone')
            userprofile.address=request.POST.get('address')
            userprofile.city=request.POST.get('city')
            userprofile.state=request.POST.get('state')
            userprofile.country=request.POST.get('country')
            userprofile.pincode=request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user=request.user
        neworder.fname=request.POST.get('fname')
        neworder.lname=request.POST.get('lname')
        neworder.email=request.POST.get('email')
        neworder.phone=request.POST.get('phone')
        neworder.address=request.POST.get('address')
        neworder.city=request.POST.get('city')
        neworder.state=request.POST.get('state')
        neworder.country=request.POST.get('country')
        neworder.pincode=request.POST.get('pincode')

        neworder.payment_mode = request.POST.get('payment_mode') 
        ticket = Ticket.objects.filter(user=request.user) 
        ticket_total_price=0
        for item in ticket:
            ticket_total_price=ticket_total_price+item.movie.selling_price*item.ticket_qty

        neworder.total_price=ticket_total_price 
        trackno = 'towhid' +str(random.randint(1111111,9999999)) 

        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'towhid' +str(random.randint(1111111,9999999)) 
        neworder.tracking_no=trackno
        neworder.save()

        neworderitems = Ticket.objects.filter(user=request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                movie = item.movie,
                price = item.movie.selling_price,
                quantity = item.ticket_qty,
            )
            #To decrease the movie quantity from available stock
            orderticket=Movie.objects.filter(id=item.movie_id).first()
            orderticket.quantity = orderticket.quantity-item.ticket_qty
            orderticket.save()

        #To clear user's ticket
        Ticket.objects.filter(user=request.user).delete()
        messages.success(request,"Your order has been placed successfully")         

    return redirect('/')

