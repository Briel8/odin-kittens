from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Kitten
from .forms import KittenCreationForm

def index(request):
    kittens = Kitten.objects.all()
    return render(request, 'kittens/index.html', {'kittens': kittens})

def show(request, pk):
    """
    Renders a details page for a single kitten.
    """
    kitten = get_object_or_404(Kitten, id=pk)
    return render(request, 'kittens/show.html', {'kitten': kitten})

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