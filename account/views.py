from sqlite3 import Time
from turtle import title
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
import copy
from itertools import chain
from datetime import date, timedelta




class Login(ListView):
    queryset = Article.objects.all()
    template_name = "login.html"    
	
class ArticleList(LoginRequiredMixin, ListView):
	template_name = "home.html"

	def get_queryset(self):

		current_time = datetime.datetime.now()
		current_date = date.today().isoformat()   
		first_time = (date.today()-timedelta(days=1)).isoformat()
		second_time = (date.today()-timedelta(days=7)).isoformat()
		third_time = (date.today()-timedelta(days=30)).isoformat()
		fourth_time = (date.today()-timedelta(days=90)).isoformat()
		fifth_time = (date.today()-timedelta(days=180)).isoformat()

			
		query = Article.objects.filter(user=self.request.user)
		if self.request.user.is_superuser:
			return Article.objects.filter(user=self.request.user).\
								   filter((Q(created=current_date))\
								   |(Q(created=first_time))\
								   |(Q(created=second_time))\
								   |(Q(created=third_time))\
								   |(Q(created=fourth_time))\
								   |(Q(created=fifth_time)))
						
			
		else:
			#return Article.objects.filter(user=self.request.user).filter(Q(created__day=date_to_number(current_time)-1) | Q(created__day=date_to_number(current_time)-7) | Q(created__day=date_to_number(current_time)-30) | Q(created__day=date_to_number(current_time)-90) | Q(created__day=date_to_number(current_time)-180))
			pass
			#return Article.objects.filter(user=self.request.user).filter(Q(created=current_date))


# Create your views here.
# @login_required
# def home(request):
#     return render(request, 'home.html')

# def ArticleList(request):
# 	query = Article.objects.filter(user=request.user)
# 	current_time = datetime.datetime.now()

# 	current_date = date.today().isoformat()   
# 	days_before = (date.today()-timedelta(days=30)).isoformat()
	

# 	def date_to_number(current_time):
#  		#return  ( current_time.year *365 + current_time.month * 31 + current_time.day)
# 		return 23
# 	m = []

# 	query1 = query.distinct()

# 	for q in query1 :
# 		if q.time_created_in_day() != (date_to_number(current_time)-1):
# 			res=q.exclude()
			
		
# 	context = {
#         "data" : query,
#     }
# 	return render(request, "home.html", context)	







# class ArticleList(LoginRequiredMixin, ListView):
# 	template_name = "home.html"

# 	def get_queryset(self):
# 		current_time = datetime.datetime.now()
# 		def date_to_number(current_time):
# 			return  ( current_time.year *365 + current_time.month * 31 + current_time.day)

# 		query = Article.objects.filter(user=self.request.user)
# 		if self.request.user.is_superuser:
# 			return Article.objects.all()
# 			#return Article.objects.filter(user=self.request.user).filter(Q(created__day=date_to_number(current_time)-1) | Q(created__day=date_to_number(current_time)-7) | Q(created__day=date_to_number(current_time)-30) | Q(created__day=date_to_number(current_time)-90) | Q(created__day=date_to_number(current_time)-180))
# 		else:
# 			return Article.objects.filter(user=self.request.user).filter(Q(created__day=today-1) | Q(created__day=today-7) | Q(created__day=today-30) | Q(created__day=today-90) | Q(created__day=today-180))



class ArticleCreate(LoginRequiredMixin, CreateView):
	model = Article
	fields = ['user', 'title', 'description','created','test_int']
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




	