from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('add/<item_id>/', views.item_to_basket, name='item_to_basket'),
    path('update/<item_id>/', views.update_basket, name='update_basket'),
    path('remove/<item_id>/', views.remove_from_basket, name='remove_from_basket'),
]
