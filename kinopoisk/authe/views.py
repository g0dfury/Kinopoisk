from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import UserSignInForm, UserSignUpForm
from .models import User

# Create your views here.
class SignIn(View):
    def get(self, request):
        form = UserSignInForm()
        context = {
            'title':'Авторизация',
            'form': form,
        }
        return render(request, 'authe/signin.html', context=context)

    def post(self, request):
        form = UserSignInForm(request, request.POST)
        if len(request.POST['username']) > 0 and len(request.POST['password']) > 0:
        # if form.is_valid():
            try:
                user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
                login(request, user)
                return redirect(reverse_lazy('movies:index'))
            except:
                context = { 'form': form, 'error': 1 }
                return render(request, 'authe/signin.html', context=context) 
        else:
            context = { 'form': form, 'error': 2 }
            return render(request, 'authe/signin.html', context=context) 





class SignUp(View):                           # session based
    def get(self, request):
        form = UserSignUpForm()
        context = {
            'title':'Регистрация',
            'form':form,    
        }
        return render(request, 'authe/signup.html', context=context)

    def post(self, request):
        form = UserSignUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('authe:signin'))
        else:
            context = {'form':form}
            return render(request, 'authe/signup.html', context=context)


@method_decorator(login_required, name='get')
class Profile(View):
    def get(self, request):
        return render(request, 'authe/profile.html')


def signout(request):
    logout(request)
    return redirect(reverse_lazy('movies:index'))