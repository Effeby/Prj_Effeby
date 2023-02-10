from django.shortcuts import render, get_object_or_404, redirect
from .models import Poste
from .models import Like
from .models import Dislike
from .models import Commentaire
from.import views
from django.urls import reverse
from Blog.forms import CommentaireForm
from.import urls


# Create your views here.
def blog(request):
    posts = Poste.objects.filter(status = True)
    print(posts)
    datas = {
        'posts': posts,
    }

    return render(request, 'blog.html', datas)


def blog_details(request, post_id):
    detPost = Poste.objects.get(id = post_id)
    print(detPost)

    Comments = Commentaire.objects.filter(id = post_id)
    new_Comment = None
    if request.method == 'POST':
        comment_form = CommentaireForm(data= request.POST)
        if comment_form.is_valid():
            new_Comment = comment_form.save(commit = False)
            new_Comment.poste = detPost
            new_Comment.save()
            return redirect(reverse (views.blog_details, args=[post_id]))
    else:
        comment_form = CommentaireForm()
        print(Comments)

    datas = {
        'detPost' : detPost,
        'Comments': Comments,
        'new_Comment': new_Comment,
        'comment_form': comment_form,
    }

    return render(request, 'blog_details.html', datas)


def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
    return redirect('blog_details.html', post_id=post_id)

def dislike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        dislike.delete()
    return redirect('blog_details.html', post_id=post_id)