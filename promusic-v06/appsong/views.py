from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from appsong.models import *

# Create your views here.

# def charger_json(filename):
#     import json
#     f = open(filename, "r")
#     catalogue = json.load(f)
#     f.close()
#     return catalogue


def gen_page_principale(request):
	catalogue=Chanson.objects.all()
	categories=Categorie.objects.all()
	context={
		'titre':'Voici mon catalogue',
		'catalogue':catalogue,
		'categories':categories,
	}
	return render(request,'appsong/principale.html', context)


def gen_page_chanson(request,chanson_id):

	chanson=Chanson.objects.get(id=chanson_id)
	paroles=Texte.objects.get(chanson_id=chanson)

	# num_youtube = charger_youtube(chanson)

	context={
		'chanson':chanson,
		'url_top' : reverse('appsong:page_princ'),
		'paroles':paroles,
		#'num_youtube':num_youtube,
	}	

	return render(request,'appsong/chanson.html', context)


# def chercher_chanson(catalogue,chanson_id):
#     for element in catalogue:
#         if element["id"] == str(chanson_id):
#         	return element

#         	return None


# def charger_paroles(chanson):
#     paroles = open("appsong/paroles/" + chanson["fichier"],"r")
#     return paroles


# def charger_youtube(chanson):
# 	i=chanson["youtube"].index("v=")
# 	chanson["youtube"][i:]
# 	lien_yt= chanson["youtube"][i+2:]
# 	return lien_yt



