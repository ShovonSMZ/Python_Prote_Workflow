from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm, AccountAuthenticationForm, Change_userinfo_form
from .models import Account

# Create your views here.
@login_required
def index(request):
    return render(request, 'account/dashboard.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})


def login_view(request):
	user = request.user
	if user.is_authenticated:
		return redirect('dashboard')

	if request.POST:
		form = AccountAuthenticationForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)

			if user:
				login(request, user)
				return redirect('dashboard')
	else:
		form = AccountAuthenticationForm()

	return render(request, 'account/login.html', {'form': form})


def logout_view(request):
	logout(request)
	return redirect('dashboard')

def change_userinfo_view(request):
	if request.user:
		item = Account.objects.get(username=request.user.username)

	form = Change_userinfo_form(request.POST or None, instance=item)

	if request.method == 'POST' and form.is_valid():
		form.save()
		return redirect('dashboard')

	return render(request, 'account/change_userinfo.html', {'form': form})