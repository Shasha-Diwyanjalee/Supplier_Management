import csv
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import (
    Supplier,
    Order,
)
from .forms import (
    SupplierForm,
    OrderForm,
    OrderUpdateForm,
)


def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            email = forms.cleaned_data['email']
            contact = forms.cleaned_data['contact']
            address = forms.cleaned_data['address']

            Supplier.objects.create(name=name, email=email, contact=contact, address=address)
            return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


def update_supplier(request, value):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            supplier = Supplier.objects.get(id=value)
            supplier.name = forms.cleaned_data['name']
            supplier.email = forms.cleaned_data['email']
            supplier.contact = forms.cleaned_data['contact']
            supplier.address = forms.cleaned_data['address']

            supplier.save()
            return redirect('supplier-list')
       
    supplier = Supplier.objects.get(id=value)
    forms.fields['name'].initial = supplier.name
    forms.fields['email'].initial = supplier.email
    forms.fields['contact'].initial = supplier.contact
    forms.fields['address'].initial = supplier.address
    context = {
        'id': supplier.id,
        'form': forms
    }
    return render(request, 'store/update_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


class SupplierSearchResultsView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('supplier_search')
        context['supplier'] = Supplier.objects.filter(
            Q(id__icontains=query) | Q(name__icontains=query)
        )
        return context
#report generating
def supplier_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="supplier_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'name', 'email', 'contact', 'address'])

    suppliers = Supplier.objects.all().values_list('id', 'name', 'email', 'contact', 'address')

    for i in suppliers:
        writer.writerow(i)

    return response


def delete_supplier(request, value):
    supplier = Supplier.objects.get(id=value)
    supplier.delete()
    return redirect("/store/supplier-list")


def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            quantity = forms.cleaned_data['quantity']

            Order.objects.create(
                supplier=supplier,
                product=product,
                quantity=quantity,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)


def update_order(request, value):
    forms = OrderUpdateForm()
    if request.method == 'POST':
        forms = OrderUpdateForm(request.POST)
        if forms.is_valid():
            order = Order.objects.get(id=value)
            order.supplier = forms.cleaned_data['supplier']
            order.product = forms.cleaned_data['product']
            order.quantity = forms.cleaned_data['quantity']
            order.status = forms.cleaned_data['status']

            order.save()
            return redirect('order-list')

    order = Order.objects.get(id=value)
    forms.fields['supplier'].initial = order.supplier
    forms.fields['product'].initial = order.product
    forms.fields['quantity'].initial = order.quantity
    forms.fields['status'].initial = order.status
    context = {
        'id': order.id,
        'form': forms
    }
    return render(request, 'store/update_order.html', context)


class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


class OrderSearchResultsView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('order_search')
        context['order'] = Order.objects.filter(
            Q(id__icontains=query) | Q(product__icontains=query)
        )
        return context


def order_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="order_report.csv"'

    writer = csv.writer(response)
    writer.writerow(['id', 'supplier', 'product', 'quantity'])

    orders = Order.objects.all().values_list('id', 'supplier', 'product', 'quantity')

    for i in orders:
        writer.writerow(i)

    return response


def delete_order(request, value):
    order = Order.objects.get(id=value)
    order.delete()
    return redirect("/store/order-list")
