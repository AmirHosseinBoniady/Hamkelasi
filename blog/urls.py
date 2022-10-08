from django.urls import path 
from .views import ArticleList, Login, Adminlte

urlpatterns = [
    path('', ArticleList.as_view(), name="home"),
    path('loginn', Login.as_view(), name="login"),
    path('adminlte', Adminlte.as_view(), name="adminlte"),
]
