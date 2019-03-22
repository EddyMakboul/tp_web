from django.db import models

# Create your models here.

class Chanson(models.Model):
    groupe = models.CharField(max_length = 50, blank=True)
    titre = models.CharField(max_length = 50, blank=True)
    fichier = models.CharField(max_length = 200, blank=True)
    youtube = models.URLField(max_length = 100, default='', blank =True)
    categorie=models.ManyToManyField('appsong.Categorie')
    def __str__(self):
            return str(self.id)+'. '+self.titre+'-'+self.groupe


class Categorie(models.Model):
	nom=models.CharField(max_length = 30, blank=True)
	classe=models.CharField(max_length=20, blank=True)
	couleur=models.CharField(max_length=20, blank=True)
	def __str__(self):
            return str(self.id)+'. '+self.nom

	

class Texte(models.Model):
	chanson=models.OneToOneField('appsong.Chanson', primary_key=True, on_delete=models.CASCADE)
	paroles=models.TextField(max_length=5000)