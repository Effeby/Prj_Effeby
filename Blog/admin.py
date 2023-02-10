from django.contrib import admin
from .models import (Categorie, Tag, Poste, Commentaire, Like, Dislike)
# Register your models here.

admin.site.register(Categorie)
admin.site.register(Poste)
admin.site.register(Tag)
admin.site.register(Commentaire)
admin.site.register(Like)
admin.site.register(Dislike)
