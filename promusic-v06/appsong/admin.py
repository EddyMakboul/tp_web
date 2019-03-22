from django.contrib import admin
from appsong.models import *

# Register your models here.

class ChansonAdmin(admin.ModelAdmin):
	list_display=('id','groupe','titre','fichier','youtube')
	ordering=('id',)
	list_max_show_all=1000
	filter_horizontal = ('categorie',)

admin.site.register(Chanson,ChansonAdmin)

class CategorieAdmin(admin.ModelAdmin):
	list_display=('id','nom','classe','couleur')
	ordering=('id',)
	list_max_show_all=1000

admin.site.register(Categorie,CategorieAdmin)

class TexteAdmin(admin.ModelAdmin):
	list_display=('chanson_id','paroles')
	ordering=('chanson_id',)
	list_max_show_all=1000
admin.site.register(Texte,TexteAdmin)


		
