
def basket_contents(request):

    basket_item = []
    basket_total = 0
    basket_count = 0
    delivery_costs = 5

    grand_total = basket_total + delivery_costs

    context = {
        'basket_item': basket_item,
        'basket_total': basket_total,
        'basket_count': basket_count,
        'delivery_costs': delivery_costs,
        'grand_total': grand_total,
    }
    return context
