# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

def index(request):
		# Your existing index view logic
		return render(request, 'myapp/index.html')

def register(request):
		if request.method == 'POST':
				form = UserCreationForm(request.POST)
				if form.is_valid():
						user = form.save()
						login(request, user)
						return redirect('index')  # Redirect to the index page after registration
		else:
				form = UserCreationForm()

		return render(request, 'myapp/register.html', {'form': form})
