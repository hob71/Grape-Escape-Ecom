from django.shortcuts import render
from .forms import orderform

def checkout(request):
    basket = request.session.get('basket', {})

    order_form = orderform()
    template = checkout/checkout.html
    context = {
        'order_form': order_form
    }

    return render(request, template, context)
