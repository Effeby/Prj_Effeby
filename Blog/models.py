
from audioop import add
from distutils.command.upload import upload
import email
from email.policy import default
from enum import auto
from unittest.util import _MAX_LENGTH
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length = 150)
    description = models.TextField()

#standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return self.nom
        
class Tag(models.Model):
    nom = models.CharField(max_length = 150)

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self) :
        return self.nom 
        
class Poste(models.Model):
    User = models.CharField(max_length= 250)
    Titre = models.CharField(max_length=250)
    contenu = models.TextField()
    images = models.ImageField(upload_to = "poste")

    #standards
    status = models.BooleanField(default= True)
    date_add = models.DateTimeField(auto_now = True)
    date_update =models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.Titre

class Commentaire(models.Model) :
     nom = models.CharField(max_length = 150)
     poste = models.ForeignKey(Poste,on_delete=models.CASCADE,related_name="commentaire")
     commantaire = models.TextField()
     email = models.EmailField()
     likes = models.IntegerField(default=0)
     dislikes = models.IntegerField(default=0)
        #standards
     status = models.BooleanField(default= True)
     date_add = models.DateTimeField(auto_now = True)
     date_update =models.DateTimeField(auto_now = True)
     def __str__(self) :
        return self.nom
 

class Like(models.Model):
    like = models.IntegerField(default=0)
    post = models.ForeignKey(Poste, on_delete=models.CASCADE)

class Dislike(models.Model):
    dislike = models.IntegerField(default=0)
    post = models.ForeignKey(Poste, on_delete=models.CASCADE)

class Meta: 
    ordering = ['-date_added']