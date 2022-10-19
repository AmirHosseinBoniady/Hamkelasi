from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Article

# Register your models here.
User = get_user_model()

admin.site.register(User)

  
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user','title','description')
    search_fields = ['title',]
    



admin.site.register(Article, ArticleAdmin)
