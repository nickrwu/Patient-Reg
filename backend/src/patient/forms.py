from django import forms
from models import Patient

class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ['dob', 'appointment']

    dob = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y'),
        input_formats=('%m/%d/%Y')
    )

    appointment = forms.DateTimeField(
        widget=forms.DateInput(format='%m/%d/%Y %H:%M'),
        input_formats=('%m/%d/%Y %H:%M')
    )