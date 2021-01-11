from django.apps import AppConfig

#  def ready taken from Code Institue miniproject


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        import checkout.signals
