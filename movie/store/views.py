from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
# Create your views here.
def home(request):
    return render(request,'store/home.html')

def collections(request):
    category = Category.objects.filter(status=0)
    context={'category':category}
    return render(request,'store/collection.html',context)  

def collectionsview(request,slug):
    if(Category.objects.filter(slug=slug, status=0)):
        movies=Movie.objects.filter(category__slug=slug)
        category=Category.objects.filter(slug=slug).first()
        context={'movies':movies,'category':category}
        return render(request,'store/movies/index.html',context)
    else:
        messages.warning(request,"No such category found") 
        return redirect('collections') 

def moviesview(request,cate_slug,mov_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):

        if(Movie.objects.filter(slug=mov_slug, status=0)):
            movies = Movie.objects.filter(slug=mov_slug, status=0).first
            context ={'movies':movies}       


        else:
            messages.error(request,"No such product found")
            return redirect('collections') 

            
    else:
        messages.error(request,"No such category found")
        return redirect('collections')            

    return render(request,'store/movies/view.html',context)

