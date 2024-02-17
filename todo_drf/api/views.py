from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.


def index(request):
	tasks = Task.objects.all() #Fetch all tasks from the Task model
	form = TaskForm() # Initialize a TaskForm instance

	if request.method =='POST': # If the request method is POST, process the submitted form data
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/') # Redirect to the homepage after form submission

	context = {'tasks':tasks, 'form':form}  # Prepare the context data to be passed to the template
	return render(request, 'tasks/list.html', context) # Render the 'list.html' template with the context data

def taskUpdate(request, pk):
	task = Task.objects.get(id=pk) # Retrieve the task object with the given primary key
	form = TaskForm(instance=task) # Initialize a TaskForm instance with the data from the retrieved task object

	if request.method == 'POST': # If the request method is POST, process the submitted form data
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('/') # Redirect to the homepage after form submission

	context = {'form':form} # Prepare the context data containing the form to be passed to the template
	return render(request, 'tasks/update.html', context) # Render the 'update.html' template with the context data

def taskDelete(request, pk):
	item = Task.objects.get(id=pk)  # Retrieve the task object with the given primary key

	if request.method == 'POST': # If the request method is POST, process the submitted form data
		item.delete()
		return redirect('/') # Redirect to the homepage after form submission

	context = {'item':item} # Prepare the context data with the 'item' variable to be passed to the template
	return render(request, 'tasks/delete.html', context) # Render the 'delete.html' template with the context data
