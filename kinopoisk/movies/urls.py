from django.urls import path
from . import views

app_name = 'movies'


urlpatterns = [
    path('', views.Home.as_view(), name = 'index'),
    path('create/', views.CreateMovie.as_view(), name='create'),
]