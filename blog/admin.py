from django.contrib import admin
from django.contrib import messages
from .models import Article, Category
from django.utils.translation import ngettext

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    #list_filter = (['status'],)
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}

    
admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'slug', 'publish','category', 'status')
    #list_filter = (['status'])
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status', 'publish']
    

    @admin.action(description='اضافه کردن به انتشار یافته ها!')
    def make_published(self, request, queryset):
        updated = queryset.update(status='p')
        self.message_user(request, ngettext(
            '%d مقاله در دسته بندی منتشر شده ها قرار گرفت',
            '%d مقاله در دسته بندی منتشر شده ها قرار گرفتند.',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [make_published]

admin.site.register(Article, ArticleAdmin)
