# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import NumObject,Sounds, BlackList

class PlaceAdmin(admin.ModelAdmin):
	list_display = ('title', 'usersave')

class SoundAdmin(admin.ModelAdmin):
	list_display = ('title',)

admin.site.register(NumObject, PlaceAdmin)
admin.site.register(Sounds, SoundAdmin )
admin.site.register(BlackList)