from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from appsong.models import *
from appsong.forms import *

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
		'url_top' : reverse('appsong:nouv_chanson'),
		

	}
	return render(request,'appsong/principale.html', context)


def gen_page_chanson(request,chanson_id):

	chanson=Chanson.objects.get(id=chanson_id)
	#num_youtube = charger_youtube(chanson)
	context={
		'chanson':chanson,
		'url_top' : reverse('appsong:page_princ'),
		'url_modif':reverse('appsong:modif_chanson', args=[chanson_id]),
		#'num_youtube':num_youtube,
	}	
	try:
		paroles=Texte.objects.get(chanson_id=chanson)
		context['paroles']=paroles
	except Texte.DoesNotExist:
		pass

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

def gen_nouv_chanson(request):

	context = {
        'request' : request,    # pour debug
		'url_top' : reverse('appsong:page_princ'),
    }
	if request.method == 'POST':
		form=SaisieChansonForm(request.POST)
		if form.is_valid():
			groupe=form.cleaned_data['groupe']
			titre=form.cleaned_data['titre']
			youtube=form.cleaned_data['youtube']
			paroles=form.cleaned_data['paroles']
			liste = Chanson.objects.filter(groupe__iexact=groupe, titre__iexact=titre)
			if len(liste)==0:
				nouv=Chanson()
				nouv.groupe=groupe
				nouv.titre=titre
				nouv.youtube=youtube
				nouv.save()
				texte=Texte(chanson_id=nouv.id)
				texte.paroles=paroles
				texte.save()
				context['nc_message']='la chanson a bien été crée.'
			else:
				context['nc_message']='la chanson existe déja dans la base.'	
	else:		
		form=SaisieChansonForm()
	context['nc_form']=form

	return render(request,'appsong/nouv_chanson.html', context)


def gen_modif_chanson(request,chanson_id):

	id_check=Chanson.objects.filter(id=chanson_id)
	context = {
        'request' : request,    # pour debug
		'url_top' : reverse('appsong:page_princ'),
		'url_chanson':reverse('appsong:chanson_id', args=[chanson_id]),
    }

	if len(id_check)==1:
		if request.method == 'POST':
			form=SaisieChansonForm(request.POST)
			if form.is_valid():
				groupe=form.cleaned_data['groupe']
				titre=form.cleaned_data['titre']
				youtube=form.cleaned_data['youtube']
				paroles=form.cleaned_data['paroles']
				liste = Chanson.objects.filter(groupe__iexact=groupe, titre__iexact=titre)
				if len(liste)==0:
					modif=Chanson.objects.get(id=chanson_id)
					modif.groupe=groupe
					modif.titre=titre
					modif.youtube=youtube
					modif.save()
					texte=Texte(chanson_id=chanson_id)
					texte.paroles=paroles
					texte.save()
					context['mc_message']='la modification a bien été éffectué.'
				else:
					context['mc_message']='cette musique existe déjà.'				
		else:
			form=SaisieChansonForm()
		context['mc_form']=form			

	return render(request,'appsong/modif_chanson.html',context)		
				






