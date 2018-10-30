from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.
def index(request):
    template = 'landing/index.html'
    context = {}

    #username = request.POST['inputEmail']
    #password = request.POST['inputPassword']
    if request.POST:
        username = 'Jesse'
        password = 'P@ssw0rd1!'
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/catalog/')
    else:
        return render(request, template, context)

def signup(request):
    template = 'landing/signup.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    context = { 'form': form }
    return render(request, template, context) 

def passwordReset(email, from_email):
    template = 'registration/password_reset_email.html'
    form = PasswordResetForm({'email': email})
    return form.save(from_email=from_email, email_template_name=template)