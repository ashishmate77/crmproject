from django.contrib import admin

from .models import Customers,Products,Orders

class AdminCustomers(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile','location']

admin.site.register(Customers,AdminCustomers)
admin.site.register(Products)
admin.site.register(Orders)