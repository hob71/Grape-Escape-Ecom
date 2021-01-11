from django.shortcuts import render, reverse, redirect, get_object_or_404
from .forms import orderform
from basket.context import basket_contents
from django.conf import settings
from wines.models import Product
from .models import order, orderlineitem

import stripe

# Stripe items taken from Stripe and Code Institue miniproject


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'firstname': request.POST['firstname'],
            'lastname': request.POST['lastname'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'town': request.POST['town'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }

        order_form = orderform(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, quantity in basket.items():
                product = Product.objects.get(id=item_id)

                order_line_item = orderlineitem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    )
                order_line_item.save()

            request.session['save-profile'] = 'save-profile' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))

    else:
        basket = request.session.get('basket', {})
        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

    order_form = orderform()

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_profile = request.session.get('save_profile')
    order = get_object_or_404(order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_profile:
            profile_data = {
                'default_phone_number': order.phone_number,
                'default_country': order.country,
                'default_postcode': order.postcode,
                'default_town_or_city': order.town_or_city,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_county': order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order has been processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)