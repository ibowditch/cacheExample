from time import sleep
from django.views.generic.list import ListView
from django_tables2 import SingleTableView
from django.db.models import Q

from premier.models import Game
from .tables import GamesTable

class GamesList(ListView):
    model = Game
    template_name = 'game_list.html'

class GamesTableView(SingleTableView):
    model = Game
    table_class = GamesTable
    template_name = 'games_table_list.html'
    paginate_by = 20
    full_title = "Scottish Premier League Games"

    def get_queryset(self):
        allgames =  Game.objects.all()
        sleep(2)
        if 'team' in self.kwargs:
            allgames = allgames.filter(Q(home_team=self.kwargs['team']) | Q(away_team=self.kwargs['team']))
        return allgames
