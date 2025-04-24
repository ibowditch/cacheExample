from django.shortcuts import render

# Create your views here.

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django_tables2 import SingleTableView
from django_tables2.paginators import LazyPaginator

from premier.models import Game
from .tables import GamesTable

class GamesList(ListView):
    model = Game
    template_name = 'game_list.html'

# class GamesListTeam(ListView):
#     model = Game
#     template_name = 'game_list.html'

class GamesTableView(SingleTableView):
    model = Game
    table_class = GamesTable
    template_name = 'games_table_list.html'
    table_pagination = False
    full_title = "Games"

    def get_queryset(self):
        allgames =  Game.objects.all()
        return allgames

        # filter(curr_status__in=('1OFF', '2AFF', '3RES', '4ADM', '5TRN', '6SUP', '7LVE',))\
            # .order_by('curr_status', 'surname').select_related('mContact')