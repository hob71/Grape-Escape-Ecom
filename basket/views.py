from django.shortcuts import render, redirect, reverse


def basket(request):
    return render(request, 'basket/basket.html')


def item_to_basket(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):

    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def remove_from_basket(request, item_id):

    basket = request.session.get('basket', {})

    basket.pop(item_id)

    request.session['basket'] = basket
    return redirect(reverse('basket'))
