from django import forms
from django.forms import ModelForm


from .models import *


class TaskForm(forms.ModelForm):

    class Meta:         
        model = Task       #the model we are creating a form for
        fields = '__all__'       #specifiying the fields from the model we want to show in the form
