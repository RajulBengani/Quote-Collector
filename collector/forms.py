from django import forms
from .models import Quote
class AddForm(forms.ModelForm):
    class Meta:
        model=Quote
        fields=['quote', 'author']
        widgets={
            'quote':forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':"Enter your quote here",
                'rows':4
            }),
            'author':forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':"Enter author name here"
            })
        }
    