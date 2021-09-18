from django.shortcuts import render
from store.models import Supplier, Order


def dashboard(request):
    total_supplier = Supplier.objects.count()
    total_oder = Order.objects.count()
    orders = Order.objects.all().order_by('-id')
    context = {
        'supplier': total_supplier,
        'order': total_oder,
        'orders': orders
    }
    return render(request, 'dashboard.html', context)
