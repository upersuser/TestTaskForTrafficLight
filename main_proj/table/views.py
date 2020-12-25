from django.shortcuts import render
from .models import Post, User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    users = User.objects.all()
    context ={
        'us':users,
        'ps':posts
    }
    return render(request, 'index.html', context)
