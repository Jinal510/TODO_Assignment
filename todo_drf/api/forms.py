from django import forms
from django.forms import ModelForm

from .models import * # Import all data from models


class TaskForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'})) # Define a CharField for the title input with a placeholder attribute.

	class Meta: # Meta class for defining metadata options for the model.
		model = Task # Define the model as Task
		fields = '__all__' # Specify that all fields of the model should be included in the form