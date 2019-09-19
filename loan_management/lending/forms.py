from django import forms
from .models import Borrower

class RegistrationForm(forms.ModelForm):
	class Meta:
		model = Borrower
		fields = "__all__"