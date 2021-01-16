from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import Product
from .forms import wineform, regionform, cheeseform
# From Code Institue mini project login_required
from django.contrib.auth.decorators import login_required


def all_wines(request):

    wines = Product.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wines/wines.html', context)


@login_required
def add_wine(request):

    if request.method == 'POST':
        form = wineform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_wine'))
    else:
        form = wineform()

    form = wineform()
    template = 'wines/add_wine.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_wine(request, product_id):
    wine = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = wineform(request.POST, request.FILES, instance=wine)
        if form.is_valid():
            form.save()
            return redirect('wines')
    else:
        form = wineform(instance=wine)

    template = 'wines/edit_wine.html'
    context = {
        'form': form,
        'wine': wine,
    }

    return render(request, template, context)


@login_required
def delete_wine(request, product_id):
    wine = get_object_or_404(Product, pk=product_id)
    wine.delete()
    return redirect(reverse('wines'))


@login_required
def add_region(request):

    if request.method == 'POST':
        form = regionform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_region'))
    else:
        form = regionform()

    form = regionform()
    template = 'wines/add_region.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_cheese(request):

    if request.method == 'POST':
        form = cheeseform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_cheese'))
    else:
        form = cheeseform()

    form = cheeseform()
    template = 'wines/add_cheese.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
