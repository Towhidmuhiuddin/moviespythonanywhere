from django.http.response import JsonResponse

from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Movie, Wishlist

@login_required(login_url='login')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context={'wishlist':wishlist}
    return render(request,'store/wishlist.html',context)


def addtowishlist(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            mov_id=int(request.POST.get('movie_id'))
            movie_check=Movie.objects.get(id=mov_id)
            if(movie_check):
                if(Wishlist.objects.filter(user=request.user,movie_id=mov_id)):
                    return JsonResponse({'status':'Movie are already wishlist'})
                else:
                    Wishlist.objects.create(user=request.user, movie_id=mov_id)
                    return JsonResponse({'status':'Movie added to wishlist'})
            else:
                return JsonResponse({'status':'No such movie found'})
        else:
            return JsonResponse({'status':'login to continue'})
    return redirect('/')  

def deletewishlist(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            mov_id =int(request.POST.get('movie_id'))
            if(Wishlist.objects.filter(user=request.user, movie_id=mov_id)):
                wishlistitem = Wishlist.objects.get(movie_id=mov_id)
                wishlistitem.delete()
                return JsonResponse({'status':'Movie delete from wishlist'})
            else:
                Wishlist.objects.create(user=request.user, movie_id = mov_id)
                return JsonResponse({'status':'Movie not found in wishlist'})
        else:
            return JsonResponse({'status':'Login to Continue'}) 
    return redirect('/')        