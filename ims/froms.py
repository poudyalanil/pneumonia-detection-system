from django import forms
from ims.models import User_Support_Ticket


class Issue_New_Ticket(forms.ModelForm):
    class Meta:
        model = User_Support_Ticket
        fields = ['title', 'message']
