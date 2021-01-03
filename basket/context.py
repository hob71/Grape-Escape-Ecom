from django.shortcuts import get_object_or_404
from wines.models import Product


def basket_contents(request):

    basket_item = []
    basket_total = 0
    basket_count = 0
    delivery_costs = 5
    basket = request.session.get('basket', {})

    for item_id, quantity in basket.items():
        wine = get_object_or_404(Product, pk=item_id)
        basket_total += quantity * wine.price
        basket_count += quantity
        basket_item.append({
            'item_id': item_id,
            'quantity': quantity,
            'wine': wine,
        })

    grand_total = basket_total + delivery_costs

    context = {
        'basket_item': basket_item,
        'basket_total': basket_total,
        'basket_count': basket_count,
        'delivery_costs': delivery_costs,
        'grand_total': grand_total,
    }
    return context
