from django.shortcuts import render, redirect
from django.urls import reverse
from demoapp.forms import LogForm
from demoapp.models import Logger
# Create your views here.


def form_view(request):
    form = LogForm()
    saved_data = Logger.objects.all()
    saved_data = []  
    show_data = False 
    
    #to submit data 
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Form_Model'))

    #to show data 
    if 'show_data' in request.GET:
        saved_data = Logger.objects.all()
        show_data = True



    context = {'form': form, 'saved_data': saved_data, 'show_data': show_data}

    return render(request, "home.html", context)