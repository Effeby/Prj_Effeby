from django.contrib import admin
from .models import (Article, Contact, Panier, Categorie, Envie)
# Register your models here.
admin.site.register(Article)
admin.site.register(Contact)
admin.site.register(Panier)
admin.site.register(Categorie)
admin.site.register(Envie)