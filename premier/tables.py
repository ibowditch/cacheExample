#
# from __future__ import unicode_literals
from collections import OrderedDict

# TODO rationalise by grouping Column definitions in one place */

import django_tables2 as tables
from django.urls import reverse
from django.utils.html import format_html
from django_tables2.utils import A, Sequence
from django.db.models import F
from operator import countOf, itemgetter
from datetime import date
import re

import logging

from .models import Game

logger = logging.getLogger(__name__)


class GamesTable(tables.Table):
    # qsumm =     tables.Column(accessor='quals_str', verbose_name='Qualifications', orderable=False)       # quals_str get_qual_string
    # qsumm =     tables.Column(accessor='get_quals_string', verbose_name='Qualifications', orderable=False)       # quals_str get_qual_string
    # active =    tables.BooleanColumn(verbose_name='Active',)
    # rank =      tables.Column(accessor='field_pos',)
    # rfsID =     tables.Column(accessor='rfsID',)
    # mContact =  tables.Column(verbose_name='Name', linkify=('member-detail', [A('id')]),)
    # cMobile =   tables.Column(accessor='mContact.Mobile',)
    # email =     tables.Column(accessor='mContact.email', verbose_name='Email address')

    class Meta:
        model = Game
        # fields = ('qsumm', 'active', 'rank', 'rfsID', 'mContact', 'cMobile', 'email',)
        attrs = {'class': 'table table-sm table-striped table-hover', 'id': 'gameslist'}