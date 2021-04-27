from django import forms
from blog.models import Tags, Category, Blog
from django_summernote.widgets import SummernoteWidget

class Create_New_Tag(forms.ModelForm):
    class Meta:
        model = Tags
        fields = '__all__'

class Create_New_Category(forms.ModelForm):
    class Meta:
        model= Category
        fields = '__all__'

class Create_New_Blog(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Blog
        fields = '__all__'
        