from django import forms

from .models import  bug_inform

# class BugTypeForm(forms.ModelForm):
#     class Meta:
#         model = bug_type
#
#         fields = ['text']
#
#         labels = {'text': ''}


class BugInfromForm(forms.ModelForm):
    class Meta:
        model = bug_inform
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={"cols": 100})}
