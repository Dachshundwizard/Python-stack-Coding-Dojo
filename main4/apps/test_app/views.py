from django.shortcuts import render, redirect
from .models import Blog, Comment #getting the two classes that are in the models file
# Create your views here.
def index(request):
    context = {
    "blogs" : Blog.objects.all() #select * from blog
    }
    return render(request, "test_app/index.html", context)

def blogs(request):
    #using ORM
    Blog.objects.create(title=request.POST['title'], blog=request.POST['blog'])
    #insert into blogs (title, blog, created at, updated at) values (title, blog, now now)
    return redirect('/')
