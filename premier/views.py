from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator

from premier.models import *

class GamesList(ListView):
    model = Game
    template_name = 'game_list.html'

    # def get_context_data(self, **kwargs):  # Turn off menu for this case
    #     cont = super().get_context_data()
    #     cont['vlist'] = RFSVehicle.objects.for_brigade(self.request.tenant.schema_name)
    #     return cont