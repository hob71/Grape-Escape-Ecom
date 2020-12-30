from django.shortcuts import render
from .models import Product


def all_wines(request):

    wines = Product.objects.all()

    context = {
        'wines': wines,
    }

    return render(request, 'wines/wines.html', context)
