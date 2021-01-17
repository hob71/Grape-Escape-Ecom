from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


class StripeWH_Handler:

    def __init__(self, request):

        self.request = request

    def send_email(self, order):
        customer_email = order.customer_email
        subject = render_to_string(
            'checkout/confirmation_email/order_confirmation_email_subject.txt',{'order': order})
        body = render_to_string(
            'checkout/confirmation_email/order_confirmation_email_body.txt',{'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )

    def handle_event(self, event):

        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}',
            status=200)

    def handle_payment_succeeded(self, event):

        self._send_confirmation_email(order)
        
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_failed(self, event):

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=400)