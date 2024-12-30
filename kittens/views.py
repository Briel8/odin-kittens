from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.http import Http404
from .models import Kitten
from .forms import KittenCreationForm

def index(request):
    """
    Renders a page with kitten objects. Return a json object if an API request is made.
    """
    kittens = Kitten.objects.all()
    if request.headers.get('Accept') == 'application/json':             # API call is made
        kittens = list(Kitten.objects.values())
        return JsonResponse(kittens, safe=False)
    return render(request, 'kittens/index.html', {'kittens': kittens})  

def show(request, pk):
    """
    Renders a details page for a single kitten.
    """
    try:
        kitten = get_object_or_404(Kitten, id=pk)
        if request.headers.get('Accept') == 'application/json':              # API call is made
            return JsonResponse({'id': kitten.id, 'name': kitten.name})
        return render(request, 'kittens/show.html', {'kitten': kitten})     
    except Kitten.DoesNotExist:
        raise Http404('Kitten does not exist')


def new(request):
    """
    Renders a new Kitten creation page.
    """
    form = KittenCreationForm()
    return render(request, 'kittens/new.html', {'form': form})

def create(request):
    """
    Create a new Kitten.
    """
    form = KittenCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('kittens:index')
    return redirect('kittens:new')

def edit(request, pk):
    """
    Renders the edit kitten page with prefilled input labels.
    """
    kitten = get_object_or_404(Kitten, id=pk)
    form = KittenCreationForm(instance=kitten)
    return render(request, 'kittens/edit.html', {'form': form, 'kitten': kitten})

def update(request, pk):
    """
    Updates an existing Kitten.
    """
    kitten = get_object_or_404(Kitten, id=pk)
    form = KittenCreationForm(request.POST, instance=kitten)
    if form.is_valid():
        form.save()
        return redirect('kittens:new')
    return render(request, 'kittens/edit.html', {'form': form})

def destroy(request, pk):
    """
    Destroys an existing Kitten.
    """
    Kitten.objects.get(pk=pk).delete()
    return redirect('kittens:index')