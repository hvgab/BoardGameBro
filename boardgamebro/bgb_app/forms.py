from django import forms
from .models import Play


class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ['name', 'date', 'game', 'players', 'winner']

    # if user is in a gamenight with date = today:
    # hook this play into that gamenight, and show gamenight at top of form.
    # players should be default selected with players from gamenight, total list should be frineds of host.
