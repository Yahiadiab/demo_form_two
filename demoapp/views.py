from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from demoapp.forms import LogForm
from demoapp.models import Logger
from django.core.paginator import Paginator
from django.db.models import  Q
# Create your views here.



def testing(request):
    return render(request, "testing.html")

def form_view(request):
    form = LogForm()
    page_obj = None
    search_query=request.GET.get('search','')

    #to submit data 
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Form_Model'))

    #to show data 
    
    saved_data = Logger.objects.all()

    if search_query :
        saved_data = saved_data.filter(
            Q(first_name__icontains=search_query)|
            Q(last_name__icontains=search_query)|
            Q(age__icontains=search_query))

    paginator = Paginator(saved_data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        



    context = {'form': form, 'page_obj': page_obj,'search_query': search_query}

    return render(request, "home.html", context)


def delete_entry(request, entry_id):
    entry = get_object_or_404(Logger, id=entry_id)
    entry.delete()
    log = "hi" 
    return redirect(reverse('Form_Model'))

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


