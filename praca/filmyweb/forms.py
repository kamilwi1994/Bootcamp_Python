from django.forms import ModelForm
from .models import Film

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['tytul', 'rok', 'opis', 'premiera', 'imdb_rating', 'plakat', 'video']
