from django.views.generic import ListView
from django.shortcuts import render

from blog.models import Category, Article

# def blog(request):
#     context = {
#         "category" : Category.objects.all()
#     }
#     return render(request, 'blog.html', context)

class ArticleList(ListView):
    queryset = Category.objects.all()
    paginate_by = 4
    context_object_name = "category"
    template_name = "home.html"
    
class Home(ListView):
    queryset = Category.objects.all()
    template_name = "blog.html"

class Login(ListView):
    queryset = Category.objects.all()
    template_name = "login.html"    

class Adminlte(ListView):
    queryset = Category.objects.all()
    template_name = "home.html"    