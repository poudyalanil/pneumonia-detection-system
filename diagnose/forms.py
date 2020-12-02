from django import forms
from diagnose.models import Diagnose


class New_Test(forms.ModelForm):
    class Meta:
        model = Diagnose
        fields = ['patient_name', 'patient_country',
                  'patient_city', 'x_ray_image']
