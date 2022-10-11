from django.urls import path 
from .views import ArticleList, Login, Adminlte, Home

app_name = 'blog'
urlpatterns = [
    path('blog', ArticleList.as_view(), name="blog"),
    path('', Home.as_view(), name="home"),

    path('loginn', Login.as_view(), name="login"),
    path('adminlte', Adminlte.as_view(), name="adminlte"),
]
