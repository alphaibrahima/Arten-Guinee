from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from utilisateurs.models import *
from django.views.generic import View
from .models import Event



class EvensViews(View):
    def get(self, request):
        user = User.objects.count()
        context = {
            'user' : user,
        }
        return render(request, 'evens/addevens.html', context)

    def post(self, request):
        # Recuperation des datas
        if request.method == 'POST':
            user        = request.user
            titre       = request.POST.get('titre')
            lieu        = request.POST.get('lieu')
            date        = request.POST.get('date')
            desc        = request.POST.get('desc')
            thumbnail   = request.FILES['thumbnail']

            fesseul_obj    = Event(author=user, titre=titre, lieu=lieu, Date=date, description=desc, thumbnail=thumbnail)
            fesseul_obj.save()

            # user_count = User.objects.filter(lieu=lieu).count()
            # context = {
            #     'user' : user_count,
            # }
        return redirect('feseul')



def sommeUser(request):
    user = User.objects.all()
    context = {
        'user' : user
    }
    return render(request, 'evens/addevens.html', context)

def DelEvent(request, id):    
    post_ = get_object_or_404(Event, id=id)
    post_.delete()
    return redirect('feseul')