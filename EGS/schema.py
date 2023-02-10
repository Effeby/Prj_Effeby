# schema.py
from graphene_django import DjangoObjectType
import graphene
from graphene_file_upload.scalars import Upload
from .models import Categorie, Article, Contact, Panier, Envie

class CategorieType(graphene.ObjectType):
    class Meta:
        model = Categorie

class ArticleType(graphene.ObjectType):
    class Meta:
        model = Article

class ContactType(graphene.ObjectType):
    class Meta:
        model = Contact

class PanierType(graphene.ObjectType):
    class Meta:
        model = Panier

class EnvieType(graphene.ObjectType):
    class Meta:
        model = Envie

class Query(graphene.ObjectType):
    categorie = graphene.Field(CategorieType, id=graphene.Int())
    categories = graphene.List(CategorieType)

    article = graphene.Field(ArticleType, id=graphene.Int())
    articles = graphene.List(ArticleType)

    contact = graphene.Field(ContactType, id=graphene.Int())
    contacts = graphene.List(ContactType)

    panier = graphene.Field(PanierType, id=graphene.Int())
    paniers = graphene.List(PanierType)

    envie = graphene.Field(EnvieType, id=graphene.Int())
    envies = graphene.List(EnvieType)

    def resolve_categorie(self, info, id):
        return Categorie.objects.get(pk=id)

    def resolve_categories(self, info):
        return Categorie.objects.all()

    def resolve_article(self, info, id):
        return Article.objects.get(pk=id)

    def resolve_articles(self, info):
        return Article.objects.all()

    def resolve_contact(self, info, id):
        return Contact.objects.get(pk=id)

    def resolve_contacts(self, info):
        return Contact.objects.all()

    def resolve_panier(self, info, id):
        return Panier.objects.get(pk=id)

    def resolve_paniers(self, info):
        return Panier.objects.all()

    def resolve_envie(self, info, id):
        return Envie.objects.get(pk=id)

    def resolve_envies(self, info):
        return Envie.objects.all()

schema = graphene.Schema(query=Query)