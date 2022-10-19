from email.policy import default
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone
import datetime
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser


User = get_user_model()
class Article(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, verbose_name = "عنوان")
    description = models.TextField()
    test_int = models.IntegerField()
    created = models.DateField(default=timezone.now)
  
    class Meta:
        verbose_name ="مرور"
        verbose_name_plural = "مرورها"


    def __str__(self):
        return self.title
    
    def time_created_in_day(self):
        return  ( self.created.year *365 + self.created.month * 31 + self.created.day)

    def get_absolute_url(self):
        return ("http://127.0.0.1:8000/account")

