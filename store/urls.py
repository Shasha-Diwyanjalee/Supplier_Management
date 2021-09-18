from django.urls import path
from .views import (
    create_supplier,
    create_order,
    SupplierListView,
    OrderListView,
    SupplierSearchResultsView,
    OrderSearchResultsView,
    supplier_report,
    order_report,
    delete_supplier,
    delete_order,
    update_supplier,
    update_order,
)

urlpatterns = [
    path('create-supplier/', create_supplier, name='create-supplier'),
    path('create-order/', create_order, name='create-order'),
    path('supplier-list/', SupplierListView.as_view(), name='supplier-list'),
    path('order-list/', OrderListView.as_view(), name='order-list'),
    path('supplier-search/', SupplierSearchResultsView.as_view(), name='supplier_search'),
    path('order-search/', OrderSearchResultsView.as_view(), name='order_search'),
    path('supplier-report/', supplier_report, name='supplier-report'),
    path('order-report/', order_report, name='order-report'),
    path('supplier-list/delete/<int:value>/', delete_supplier, name='delete-supplier'),
    path('order-list/delete/<int:value>/', delete_order, name='delete-supplier'),
    path('update-supplier/<int:value>/', update_supplier, name='update-supplier'),
    path('update-order/<int:value>/', update_order, name='update-order'),
]
