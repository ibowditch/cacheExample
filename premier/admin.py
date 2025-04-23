from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import fields, resources
from import_export.widgets import DateWidget, Widget, CharWidget

from premier.models import *

# Register your models here.

class GameResource(resources.ModelResource):
    class Meta:
        model = Game

 #       import_id_fields = ('username', 'password', 'first_name', 'last_name', 'email')

class GameAdmin(ImportExportModelAdmin):
    resource_class = GameResource
  #  list_display = ('username', 'first_name', 'last_name', 'last_login')

admin.site.register(Game, GameAdmin)