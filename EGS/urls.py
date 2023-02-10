"""prjfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from EGS import views
from django.conf import settings
from  django.views.decorators.csrf  import  csrf_exempt 
from  graphene_django.views  import  GraphQLView 
from .schema import schema


urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact.html/', views.contact, name= 'contact'),
    path('politique.html/', views.politique, name= 'politique'),
    path('shop.html/', views.shop, name= 'shop'),
    path('about.html/', views.about, name= 'about'),
    path('/article/<int:pk>', views.product_details, name ="product_details"),
    path('validation.html/', views.validation, name= 'validation'),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
    #----- chemin pour les serializers -----
    #pour voir les articles
    path('articles/',views.allArticles),
    #pour voir l'article selection par l'id
    path('article/<int:id>/', views.getArticle),
    #pour ajouter un article a la base de donnée
    path('addArticle/', views.addArticle),
    #pour update un article par l'id
    path('updateArticle/', views.updateArticle),
]
