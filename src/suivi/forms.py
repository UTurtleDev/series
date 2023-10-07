from django import forms
from .models import Serie


class SerieForm(forms.ModelForm):
    class Meta:
        model = Serie
        fields = ['seen_seasons', 'number_of_seasons']

    def clean(self):
        cleaned_data = super().clean()
        seen_seasons = cleaned_data.get('seen_seasons')
        number_of_seasons = cleaned_data.get('number_of_seasons')

        if seen_seasons and number_of_seasons and seen_seasons > number_of_seasons:
            raise forms.ValidationError("The number of seen seasons cannot be greater than the total number of seasons.")

        if number_of_seasons is not None and seen_seasons is not None:
            if number_of_seasons < seen_seasons:
                raise forms.ValidationError("The number of seasons cannot be less than the number of seen seasons.")

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Name cannot be empty.")
        return name

    def clean(self):
        cleaned_data = super().clean()
        seen_seasons = cleaned_data.get('seen_seasons')
        number_of_seasons = cleaned_data.get('number_of_seasons')

        if seen_seasons is not None and seen_seasons < 0:
            self.add_error('seen_seasons', 'Seen seasons cannot be negative.')

        if number_of_seasons is not None and number_of_seasons < 0:
            self.add_error('number_of_seasons', 'Number of seasons cannot be negative.')

        return cleaned_data
