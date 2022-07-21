from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View

from AnnonceEtpse.models import *
from utilisateurs.models import *
from Postfeeds.models import *
from django.db.models import Q
from evenadmin.models import *
from xamxam.models import *
from event.models import *
from .models import *
from django.db.models.aggregates import Sum

# Create your views here.
class ReportinView(View):
    def get(self, request):
        postfeed     = Feseul.objects.all()
        posts        = Post.objects.all()
        users        = User.objects.all()
        profiles     = Profile.objects.all()
        pages        = Page.objects.all()
        xamxam       = Xamxam.objects.all()
        evens        = Event.objects.all()
        evens_views  = Event.objects.aggregate(Sum('views'))
        
        adminEvens   = EvenementAdmin.objects.all()
        # adminViews   = EvenementAdmin.objects.aggregate(Sum('views'))
        post_like    = Feseul.objects.all().count()
        associations = Association.objects.all()

        context = {
           # Types de postes 
            'postfeed'     : postfeed,
            'xamxam'       : xamxam,
            'posts'        : posts,
            'post_like'    : post_like,

            # Utilisateurs et ses types
            'associations' : associations,
            'profiles'     : profiles,
            'pages'        : pages,
            'users'        : users,

            'evens_views' : evens_views,

            # les evenements
            'adminEvens'   : adminEvens,
            'evens'        : evens,
        }

        return render(request, 'etat_senegal/reporting.html', context)










# Create your views here.
# class ReportinView(View):
#     def get(self, request):
#         # Recuperation de tout les Posts et ses differends types
#         # postfeed   = Feseul.objects.all()
#         # xamxam     = Xamxam.objects.all()
#         # posts      = Post.objects.all()

#         # Recuperation des likes de tous le posts
#         # post_like   = Feseul.objects.all().count()

#         # Recuperation de tout les utilisateurs et ses differends types
#         users        = User.objects.all()
#         pages        = Page.objects.all()
#         profiles     = Profile.objects.all()
#         associations = Association.objects.all()
        
#         # Recuperation des evenements
#         adminEvens   = EvenementAdmin.objects.all()
#         evens        = Event.objects.all()

#         context = {
#             # Types de postes 
#             'postfeed'     : postfeed,
#             'xamxam'       : xamxam,
#             'posts'        : posts,
#             'post_like'    : post_like,

#             # Utilisateurs et ses types
#             'associations' : associations,
#             'profiles'     : profiles,
#             'pages'        : pages,
#             'users'        : users,

#             # les evenements
#             'adminEvens'   : adminEvens,
#             'evens'        : evens,
#         }

#         return render(request, 'etat_senegal/reporting.html', context)