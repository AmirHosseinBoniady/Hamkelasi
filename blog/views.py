from django.views.generic import ListView
from django.shortcuts import render

from blog.models import  Article

class ArticleList(ListView):
    paginate_by = 4
    context_object_name = "category"
    template_name = "home.html"
    
class Home(ListView):
    queryset = Article.objects.all()
    template_name = "blog.html"

class Login(ListView):
    queryset = Article.objects.all()
    template_name = "login.html"    

class Adminlte(ListView):
    queryset = Article.objects.all()
    template_name = "home.html"    