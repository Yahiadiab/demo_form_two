from django.shortcuts import render, redirect, get_object_or_404
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


def delete_entry(request, entry_id):
    entry = get_object_or_404(Logger, id=entry_id)
    entry.delete()
    return redirect(f"{reverse('Form_Model')}?show_data=true")

def update_entry(request, entry_id):
    entry = get_object_or_404(Logger, id=entry_id)
    if request.method == "POST":
        form = LogForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect(reverse('Form_Model'))
    else:
        form = LogForm(instance=entry)
    return render(request, "update.html", {"form": form, "entry_id": entry_id })


