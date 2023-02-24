from django.urls import path
from store import views
from store.controller import authview,ticket,wishlist,checkout

urlpatterns = [
    path('',views.home,name='home'),
    path('collections/',views.collections, name='collections'),
    path('collections/<str:slug>',views.collectionsview, name='collectionsview'),
    path('collections/<str:cate_slug>/<str:mov_slug>',views.moviesview, name='movieview'),

    path('register/', authview.registerpage, name='register'),
    path('login/', authview.loginpage, name='login'),
    path('logout/', authview.logoutpage, name='logout'),

    path('add-to-ticket',ticket.addtoticket, name='addtoticket'),
    path('ticket',ticket.ticketview, name='ticket'),
    path('update-ticket',ticket.updateticket, name='updateticket'),
    path('delete-ticket',ticket.deleteticket, name='deleteticket'),

    path('wishlist',wishlist.index, name='wishlist'),
    path('add-to-wishlist',wishlist.addtowishlist, name='addtowishlist'),
    path('delete-wishlist',wishlist.deletewishlist, name='deletewishlist'),
    
    path('checkout',checkout.index, name='checkout'),
    path('ticket-order',checkout.ticketorder, name='ticketorder'),

]
