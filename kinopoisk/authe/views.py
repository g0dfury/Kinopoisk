from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy

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
        pass



class SignUp(View):
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
            return redirect(reverse_lazy('authe:profile'))
        else:
            context = {'form':form}
            return render(request, 'authe/signup.html', context=context)



class Profile(View):
    def get(self, request):
        
        return render(request, 'authe/profile.html')