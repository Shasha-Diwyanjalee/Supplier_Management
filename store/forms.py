from django import forms
from .models import Order


class SupplierForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    contact = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'contact',
        'data-val': 'true',
        'data-val-required': 'Please enter contact',
    }))
    address = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))


class SupplierEditForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'data-val': 'true',
        'data-val-required': 'Please enter name',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'email',
        'data-val': 'true',
        'data-val-required': 'Please enter email',
    }))
    contact = forms.CharField(widget=forms.NumberInput(attrs={
        'class': 'form-control',
        'id': 'contact',
        'data-val': 'true',
        'data-val-required': 'Please enter contact',
    }))
    address = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'id': 'address',
        'data-val': 'true',
        'data-val-required': 'Please enter address',
    }))


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'supplier', 'product', 'quantity'
        ]

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'product': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product',
                'data-val': 'true',
                'data-val-required': 'Please enter Product'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'quantity',
                'data-val': 'true',
            })
        }


class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'supplier', 'product', 'quantity', 'status'
        ]

        widgets = {
            'supplier': forms.Select(attrs={
                'class': 'form-control', 'id': 'supplier'
            }),
            'product': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product',
                'data-val': 'true',
                'data-val-required': 'Please enter Product'
            }),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'quantity',
                'data-val': 'true',
                'data-val-required': 'Please enter Quantity'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'status',
                'data-val': 'true',
            }, choices=[('decline', 'Decline'), ('approved', 'Approved'), ('processing', 'Processing'), ('complete', 'Complete')])
        }
