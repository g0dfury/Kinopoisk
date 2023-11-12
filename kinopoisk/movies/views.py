from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy

from .forms import *
from .models import *

# Create your views here.

class Home(View):
    def get(self, request):
        movies = Movie.objects.all()

        context = {
            'title': 'Все фильмы',
            'movies': movies
        }

        return render(request, 'movies/index.html', context=context)


class CreateMovie(View):
    def get(self, request):
        form = MovieCreationForm
        context = {
            'title': 'Создать фильм',
            'form': form
        }

        return render(request, 'movies/create.html', context=context)

    def post(self, request):
        form = MovieCreationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('movies:index'))

        else:
            context = {'title': 'Создать фильм','form': form, 'error': 1,}
            return render(request, 'movies/create.html', context=context)