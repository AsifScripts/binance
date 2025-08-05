from django.urls import path
from .views import dashboard, place_order_view, order_status_view, cancel_order_view

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('place_order/', place_order_view, name='place_order'),
    path('order_status/', order_status_view, name='order_status'),
    path('cancel_order/', cancel_order_view, name='cancel_order'),
]