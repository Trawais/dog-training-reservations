from django import forms

class ParticipantForm(forms.Form):
    name = forms.CharField(label="Jmeno tymu", max_length=100)
    phone_number = forms.CharField(label="Telefonni cislo", max_length=20, required=False)
    note = forms.CharField(label="Poznamka", max_length=200, required=False)
