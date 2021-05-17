from django import forms
from django.forms import ModelForm

from France.models import France


class FranceForm(ModelForm):
    class Meta:
        model = France
        fields = ["lambert_x","lambert_y","region","departement","commune","nom_du_site","date_debut","date_fin","periodes","themes","type_intervention"]

    def __init__(self, *args, **kwargs):
        super(FranceForm, self).__init__(*args, **kwargs)
