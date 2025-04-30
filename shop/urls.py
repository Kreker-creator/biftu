from django.urls import path, include
from . import views


urlpatterns = [
path('index/', views.index, name='index'),
path('about/', views.about, name='about'),
path('products/', views.products, name='products'),
path('contact/', views.contact, name='contact'),
path('success/', views.success, name='success'),
path('client_orders/', views.client_orders, name='client_orders'),
path('orders/chart/', views.order_stats, name='order_stats'),
path('sales_entry/', views.sales_entry, name='sales_entry'),
]