from django.shortcuts import render
from wines.models import Product


def index(request):
    wines = Product.objects.all()

    context = {
        'wines': wines,
    }
    return render(request, 'home/index.html', context)
