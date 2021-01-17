# signals.py taken from Code Institue miniproject


from .models import orderlineitem
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


@receiver(post_save, sender=orderlineitem)
def update_on_save(sender, instance, created, **kwargs):
    instance.order.update_total()


@receiver(post_delete, sender=orderlineitem)
def update_on_delete(sender, instance, **kwargs):
    instance.order.update_total()
