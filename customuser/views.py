from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from customuser.models import MyUser
from customuser.forms import SignInForm, SignUpForm
from courier import settings

# Create your views here.
@login_required
def index(request):
    info = settings.AUTH_USER_MODEL
    return render(request, 'index.html', {'info': info})


def signin(request):
    html = 'generic_form.html'

    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get('username'),
                password=data.get('password'))
        if user:
            login(request, user)
            return HttpResponseRedirect(
                request.GET.get('next', reverse('home')))
    form = SignInForm()
    return render(request, html, {'form': form})


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


def signup(request):
    html = 'generic_form.html'

    if request.method == 'GET':
        form = SignUpForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data
            MyUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display_name=data['display_name'],
                age=data['age'],
                homepage=data['homepage']
            )
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()
    return render(request, html, {'form': form})
