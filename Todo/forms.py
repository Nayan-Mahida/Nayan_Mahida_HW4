from django import forms
from .models import Todo

class TodoForms(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task_name']

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add tasks"
            })
        }
class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

        widgets = {
            'task_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'completed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch',
            })
        }