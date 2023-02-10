from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

#--------------------------------------------------------------------------
#Pour l'application vente: 

class Categorie(models.Model):
    nom = models.CharField(max_length = 150)

#standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return self.nom

class Article(models.Model) :
    titre = models.CharField(max_length = 150)
    description = models.TextField()
    image = models.ImageField(upload_to = "article")
    prix = models.TextField()
    quantite = models.IntegerField(default=0)
    NCategorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,related_name="categorie")
   
    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return self.titre


class Contact(models.Model):
    nom= models.CharField(max_length= 250)
    email= models.EmailField()
    suject= models.TextField()
    text= models.TextField()

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.nom


class Panier(models.Model):
    article = models.CharField(max_length=250)
    auth = models.CharField(max_length=250)
    quantite = models.IntegerField(default=0)

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.article


class Envie(models.Model):
    like = models.BooleanField()
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name="avis")
    # user = models.OneToOneField(Article,related_name="avis")
     #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return "like" 

#Fin application vente