from django import forms

class ParticipantForm(forms.Form):
    name = forms.CharField(label='Jméno týmu', max_length=100)
    phone_number = forms.CharField(label='Telefonní číslo', max_length=20, required=False)
    note = forms.CharField(label='Poznámka', max_length=200, required=False)
    password = forms.CharField(label='Heslo (povinné)', required=False)
