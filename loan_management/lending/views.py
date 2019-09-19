from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Borrower
from django.urls import reverse_lazy
from .forms import RegistrationForm
# Create your views here.

def index(request):
	template = 'list.html'
	borrowers = Borrower.objects.all()
	context = {
		'borrowers': borrowers,
	}

	return render(request, template, context)

def new_borrower(request):
	template = "new_borrower.html"

	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('lending:index'))

	else:
		context = {
			'registration_form': RegistrationForm(),
		}
	return render(request, template, context)


def delete_borrower(request, borrower_id):
	borrower = Borrower.objects.get(id=int(borrower_id))
	borrower.delete()
	return HttpResponseRedirect(reverse_lazy('lending:index'))

def update_customer_info(request, borrower_id):
	template = "update_customer_info.html"
	borrower = Borrower.objects.get(id=int(borrower_id))

	if request.method == "POST":
		form = RegistrationForm(request.POST, instance = borrower)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('lending:index'))

	else:
		context = {
			'registration_form': RegistrationForm(instance = borrower)
		}
	return render(request, template, context)

def view_customer_info(request, borrower_id):
	template = "view_customer_info.html"
	borrower = Borrower.objects.get(id=int(borrower_id))
	context = {
		'borrower': borrower,
		}
	return render(request, template, context)
