from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.# a request comes in, we send a response.
from .models import Post
def create(request):
    return HttpResponse("<h1>Create</h1>")

def detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = { #calling this dictonary "context"
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def list(request):
    queryset = Post.objects.all() # This is grabbing all information from the queries made into sqlite3 from the shell
    context = {             #calling this dictonary "context"
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def update(request):
    return HttpResponse("<h1>Update</h1>")

def delete(request):
    return HttpResponse("<h1>Delete</h1>")
