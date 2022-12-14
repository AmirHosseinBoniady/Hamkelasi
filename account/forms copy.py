from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


# Create your forms here.
User = get_user_model()
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email","phone","first_name","last_name", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user