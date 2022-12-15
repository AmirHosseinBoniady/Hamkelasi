from django.urls import path 
from .views import ArticleList, Adminlte, Home

app_name = 'blog'
urlpatterns = [
    path('blog', ArticleList.as_view(), name="blog"),
    path('', Home.as_view(), name="home"),
    path('adminlte', Adminlte.as_view(), name="adminlte"),
]
