from django.shortcuts import render
from django.http import HttpResponse

def charger_json(filename):
	import json
	f=open(filename,"r")
	catalogue=json.load(f)
	f.close()
	return catalogue

def gen_page_principale(request):
	catalogue= charger_json("appsong/catalogue.json")
	categories= charger_json("appsong/categories.json")
	
	context={
		'titre': 'Catalogue de chansons',
		'cata': catalogue,
		'cate':categories,
			}
	return render(request,'appsong/principale.html',context)


def gen_page_chanson(request, chanson_id):

	catalogue= charger_json("appsong/catalogue.json")
	chanson=chercher_chanson(catalogue,chanson_id)
	paroles=charger_parole(chanson)
	paroles=paroles.read()
	context={
		'chanson':chanson,
		'paroles':paroles,
			}
	return render(request,'appsong/chanson.html',context)


def chercher_chanson(catalogue,chanson_id):

	for element in catalogue:
		if element['id'] == str(chanson_id):
			return element

			return None

def charger_parole(chanson):
	paroles=open("appsong/"+chanson["fichier"],"r")
	return paroles


	




    
