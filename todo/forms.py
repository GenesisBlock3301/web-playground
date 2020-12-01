from django import forms
from .models import Task


class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(
                attrs={'type': "text", 'class': "form-control", 'id': "title", 'placeholder': "title"}),
            'description': forms.Textarea(attrs={'class': "form-control", 'id': "detail", 'rows': "3"})
        }
