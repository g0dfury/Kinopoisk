from django import forms

from .models import Movie

class MovieCreationForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'poster': forms.FileInput(attrs={'class': 'form-control'}),
            'trailer_url': forms.TextInput(attrs={'class': 'form-control'}),
            'title_ru': forms.TextInput(attrs={'class': 'form-control'}),
            'title_orig': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'publish_year': forms.TextInput(attrs={'class': 'form-control'}),
            'timing': forms.TextInput(attrs={'class': 'form-control'}),
            'premier_date': forms.TextInput(attrs={'class': 'form-control'}),
            'genre': forms.Select(attrs={'class': 'form-select'}),
            'country': forms.Select(attrs={'class': 'form-select'}),
            'director': forms.Select(attrs={'class': 'form-select'}),
        }