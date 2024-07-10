import django
from django.contrib import admin
from teams.models import team
# Register your models here .

@admin.register(team)
class TeamAdmin(admin.ModelAdmin):
    list_display= ['id', 'teamname', 'description', 'creationtime', 'admin', 'display_members']
