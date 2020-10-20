from django import forms
from .models import Playthrough


class PlaythroughForm(forms.ModelForm):
    class Meta:
        model = Playthrough
        fields = ['name', 'date', 'game', 'players', 'winner']

    # if user is in a gamenight with date = today:
    # hook this play into that gamenight, and show gamenight at top of form.
    # players should be default selected with players from gamenight, total list should be friends of host.


class MiniPlaythroughForm(forms.ModelForm):
    class Meta:
        model = Playthrough
        fields = ['game', 'players', 'winner']
