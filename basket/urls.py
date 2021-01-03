from django.urls import path
from . import views

urlpatterns = [
    path('basket/', views.basket, name='basket'),
    path('add/<item_id>/', views.item_to_basket, name='item_to_basket'),
]
