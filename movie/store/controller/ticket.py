from django.http.response import JsonResponse

from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from store.models import Movie, Ticket

def addtoticket(request):
    if request.method =='POST':
        if request.user.is_authenticated:
            mov_id = int(request.POST.get('movie_id'))
            movie_check = Movie.objects.get(id=mov_id)

            if(movie_check):
                if(Ticket.objects.filter(user=request.user.id,movie_id=mov_id)):
                    return JsonResponse({'status':'Movie are already in ticket'})
                else:
                    tick_qty =int(request.POST.get('ticket_qty'))

                    if movie_check.quantity >= tick_qty:
                        Ticket.objects.create(user=request.user,movie_id=mov_id,ticket_qty=tick_qty)
                        return JsonResponse({'status':'Ticket added Successfully!'})
                    else:
                        return JsonResponse({'status':'Only '+str(movie_check.quantity) +'tickets are available'})

            else:
                return JsonResponse({'status':'No such movie found'})    

        else:
            return JsonResponse({'status':'Login to continue'})
    return redirect('/')   

@login_required(login_url='login')
def ticketview(request):
    ticket=Ticket.objects.filter(user=request.user)
    context={'ticket':ticket}
    return render(request,'store/ticket.html',context) 

def updateticket(request):
    if request.method =='POST':
        mov_id=int(request.POST.get('movie_id'))
        if(Ticket.objects.filter(user=request.user, movie_id=mov_id)):
            tick_qty=int(request.POST.get('ticket_qty'))
            ticket=Ticket.objects.get(movie_id=mov_id,user=request.user)
            ticket.ticket_qty=tick_qty
            ticket.save()
            return JsonResponse({'status':'update successfully'})
    return redirect('/')

def deleteticket(request):
    if request.method == 'POST':
        mov_id=int(request.POST.get('movie_id'))
        if(Ticket.objects.filter(user=request.user, movie_id=mov_id)):
            ticketitem=Ticket.objects.get(movie_id=mov_id, user=request.user)
            ticketitem.delete()
            return JsonResponse({'status':'Deleted successfully'})
    return redirect('/') 