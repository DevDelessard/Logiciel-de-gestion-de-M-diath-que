from django import forms
from .models import Membre, Media, Emprunt

class EmpruntForm(forms.ModelForm):
    media_choices = Media.TYPE_CHOICES  # Utilisation des choix définis dans Media
    media_type = forms.ChoiceField(choices=media_choices, label="Type de média", required=True)
    media = forms.ModelChoiceField(queryset=Media.objects.none(), label="Média", required=True)

    class Meta:
        model = Emprunt
        fields = ['media_type', 'media', 'date_emprunt']

    def __init__(self, *args, **kwargs):
        super(EmpruntForm, self).__init__(*args, **kwargs)
        self.fields['media'].queryset = Media.objects.filter(disponible=True)  # Afficher uniquement les médias disponibles


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['nom', 'email']

