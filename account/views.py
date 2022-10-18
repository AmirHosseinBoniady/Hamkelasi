from sqlite3 import Time
from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from blog.models import Article
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from datetime import date
import datetime

# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'home.html')
class ArticleList(LoginRequiredMixin, ListView):
	template_name = "home.html"


	def get_queryset(self):
		tcurrent_time = datetime.datetime.now()
		today = tcurrent_time.day
		today = 13000
		query = Article.objects.filter(user=self.request.user)
		if self.request.user.is_superuser:
			return Article.objects.filter(user=self.request.user).filter(Q(created__day=today-1) | Q(created__day=today-7) | Q(created__day=today-30) | Q(created__day=today-90) | Q(created__day=today-180))
		else:
			return Article.objects.filter(user=self.request.user).filter(Q(created__day=today-1) | Q(created__day=today-7) | Q(created__day=today-30) | Q(created__day=today-90) | Q(created__day=today-180))



class ArticleCreate(LoginRequiredMixin, CreateView):
	model = Article
	fields = ['user', 'title', 'slug', 'category', 'description','thumbnail','status' ]
	template_name = "article-create.html" 


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("account:home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})