from django.shortcuts import render, redirect
from EGS.formContact import ContactForm
from .models import Article
from .models import Panier
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, auth
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

# Create your views here.
@api_view(['GET'])
def allArticles(request):
    articles = Article.objects.all()
    serialisation = ArticleSerializer(articles, many=True)
    return Response(serialisation.data)
#--------------------------------
@api_view(['GET'])
def getArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
#--------------------------------
@api_view(['POST'])
def addArticle(request):
    serializer = ArticleSerializer(data = request.data, many= True)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)
#--------------------------------
@api_view(['PUT'])
def updateArticle(request, id):
    article = Article.objects.get(id=id)
    serializer = ArticleSerializer(instance= article, data = request.data, many= True)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)



def index(request):
    paniers = Panier.objects.filter()
    articles = Article.objects.filter()
    print(paniers)
    datas = {
       'paniers ' :paniers,
       'articles':articles,
    }

    return render(request, 'index.html', datas)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        print("Votre Message a bien été envoyé")
    else:
        form = ContactForm()

    datas = {
        'form': form,
    }

    return render(request, 'contact.html', datas)


def shop(request):
    articles = Article.objects.filter()
    datas = {
        'articles':articles,
    }

    return render(request, 'shop.html', datas)


def product_details(request, pk):
    article = Article.objects.get(id=pk)
    user = request.user
    if request.method == 'POST':
        auth = user.username
        articles = article.titre
        quantite = request.POST.get('quantite')
        panier = Panier()

        panier.auth=auth
        panier.article=articles
        panier.quantite=quantite
        
        panier.save()
        return redirect('shop')
    
    datas = {
        'article': article,
        'user': request.user,
    }
    return render(request, 'product_details.html', datas)



def about(request):

    datas = {

    }

    return render(request, 'about.html', datas)



def politique(request):

    datas = {
        
    }

    return render(request, 'politique.html', datas)


def validation(request):
    validPanier = Panier.objects.filter(auth=User.username)
    print(validPanier)
    datas = {
        'validPanier':validPanier,
    }

    return render(request, 'validation.html', datas)