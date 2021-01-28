from django.shortcuts import render, redirect
from .models import Orders, Products, Customers
from .forms import ProductForm


def home(request):
    orders = Orders.objects.all()
    customers = Customers.objects.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count()

    context = {'orders': orders,
               'total_orders': total_orders,
               'pending_orders': pending_orders,
               'delivered_orders': delivered_orders,
               'outfordelivery_orders': outfordelivery_orders,
               'customers': customers}

    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Products.objects.all()
    context = {'products': products}
    return render(request, 'accounts/product.html', context)


def orders(request):
    return render(request, 'accounts/orders.html')


def customer(request, pk):
    customers = Customers.objects.get(id=pk)
    orders = customers.order_set.all()

    total_orders = len(orders)
    pending_orders = orders.filter(status='Pending').count()
    delivered_orders = orders.filter(status='Delivered').count()
    outfordelivery_orders = orders.filter(status='Outfordelivery').count()

    context = {'customers': customers,
               'orders': orders,
               'total_orders': total_orders,
               'pending_orders': pending_orders,
               'delivered_orders': delivered_orders,
               'outfordelivery_orders': outfordelivery_orders}

    return render(request, 'accounts/customer.html', context)


def all_customers(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request, 'accounts/all_customers.html', context)


def add_product(request):
    form = ProductForm()
    context = {'form': form}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        return render(request, 'accounts/add_product.html', context)


def update_product(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {'form': form}

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        return render(request, 'accounts/update_product.html', context)


def delete_product(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    return redirect('/product')

