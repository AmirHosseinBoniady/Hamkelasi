from email.policy import default
from enum import unique
from random import choices
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="ایانمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = " دسته بندی ها"
        ordering = ['position']
    
    def __str__(self):
        return self.title

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'اسپم'),
        ('p', 'منتشرشده'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, verbose_name = "عنوان")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    category = models.ForeignKey(Category, verbose_name="دسته بندی", on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    class Meta:
        verbose_name ="مقاله"
        verbose_name_plural = "مقالات"


    def __str__(self):
        return self.title

    def thumbnail_tag(self):
        return format_html("<img width=100 src='{}'>".format(self.thumbnail.url))


