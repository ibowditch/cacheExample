from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from import_export import fields, resources

from premier.models import *

class GameResource(resources.ModelResource):
    class Meta:
        model = Game

class GameAdmin(ImportExportModelAdmin):
    resource_class = GameResource

admin.site.register(Game, GameAdmin)