from app.models import Patient,Consult
from django import forms

class PatientForm(forms.ModelForm):

    class Meta():

        model = Patient
        fields = "__all__"

class ConsultForm(forms.ModelForm):

    class Meta():

        model = Consult
        fields = "__all__"


