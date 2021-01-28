from django.urls import path
from django.contrib import admin
from crmapps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('product/',views.product,name='product'),
    path('order/',views.orders, name='order'),
    path('customer/<pk>',views.customer,name='customer'),
    path('all_customers/',views.all_customers,name='all_customers'),

    path('add_product',views.add_product, name = 'add_product'),
    path('update_product/<pk>',views.update_product, name='update_product'),
    path('delete_product/<pk>',views.delete_product, name = 'delete_product')
]