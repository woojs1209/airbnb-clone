from django.views.generic import ListView, DetailView
from . import models 

class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    context_object_name = "rooms"

class RoomDetail(DetailView):
    
    model = models.Room