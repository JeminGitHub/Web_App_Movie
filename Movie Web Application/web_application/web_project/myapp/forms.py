
from django import forms
from .models import Movie

class DateInput(forms.DateInput):
    input_type = 'date'

class AddMovies(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

        widgets = {
            'year':DateInput

        }
        labels = {
            'name':"Movie Name:",
             'desc':"Movie Description",
             'year':"Movie Year",
              'img':"Move Poster"
        }


