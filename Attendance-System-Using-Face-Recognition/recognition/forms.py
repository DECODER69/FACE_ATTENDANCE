from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
#from django.contrib.admin.widgets import AdminDateWidget

class usernameForm(forms.Form):
	username=forms.CharField(max_length=30)



class DateForm(forms.Form):
	date=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))


class UsernameAndDateForm(forms.Form):
	username = forms.ModelChoiceField(queryset=User.objects.all())

	# my_field = forms.CharField(widget=forms.TextInput(attrs={'class': 'my-class'}))
	# username=forms.CharField(max_length=30)
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))


	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['date_to'].widget.attrs['class'] = 'date_to'
		self.fields['username'].widget.attrs['class'] = 'username'
		self.fields['date_from'].widget.attrs['class'] = 'date_from'



class DateForm_2(forms.Form):
	date_from=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))
	date_to=forms.DateField(widget = forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")))

       


# class reg_form(forms.Form):
# 	username = forms.CharField(max_length=12)
# 	password = forms.PasswordInput()

