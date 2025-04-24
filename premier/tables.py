import django_tables2 as tables
import logging
from .models import Game

logger = logging.getLogger(__name__)

class GamesTable(tables.Table):
    fixture_date = tables.Column(verbose_name='Date')
    home_team = tables.Column(verbose_name='Home')
    score = tables.TemplateColumn(template_code="{{ record.home_score }} - {{ record.away_score }}", orderable=False)
    away_team = tables.Column(verbose_name='Away')

    class Meta:
        model = Game
        fields = ("fixture_date", "home_team", "score", "away_team")
        attrs = {'class': 'table table-sm table-striped table-hover', 'id': 'gameslist'}