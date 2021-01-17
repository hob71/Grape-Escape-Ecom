from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from .forms import orderform
from basket.context import basket_contents
from django.conf import settings
from wines.models import Product
from .models import order, orderlineitem
from profiles.models import UserProfile
from profiles.forms import profileform
from django.contrib import messages
from django.views.decorators.http import require_POST

import stripe

# Stripe items taken from Stripe and Code Institue tutorial


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

        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            order_form = orderform(initial={
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'town': profile.default_town,
                    'postcode': profile.default_postcode,
                    'county': profile.default_county,
                    'country': profile.default_country,
                })
        else:
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
    my_order = get_object_or_404(order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        my_order.user_profile = profile
        my_order.save()

        if save_profile:
            profile_data = {
                'default_phone_number': my_order.phone_number,
                'default_country': my_order.country,
                'default_postcode': my_order.postcode,
                'default_town_or_city': my_order.town_or_city,
                'default_street_address1': my_order.street_address1,
                'default_street_address2': my_order.street_address2,
                'default_county': my_order.county,
            }
            user_profile_form = profileform(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

# message taken from Code Institute tutorial
    messages.success(request, f'Order has been processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {my_order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': my_order,
    }

    return render(request, template, context)


@require_POST
def cache_checkout_data(request):
    pid = request.POST.get('client_secret').split('_secret')[0]
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.PaymentIntent.modify(pid, metadata={
        'username': request.user,
        'save_details': request.POST.get('save-details',)
#        'basket': json.dumps(request.session.get(basket, {})),
    })
    return HttpResponse(status=200)
