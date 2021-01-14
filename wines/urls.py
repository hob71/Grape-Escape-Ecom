from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_wines, name='wines'),
    path('add/', views.add_wine, name='add_wine'),
    path('edit/<product_id>/', views.edit_wine, name='edit_wine'),
    path('delete/<product_id>/', views.delete_wine, name='delete_wine'),
]
