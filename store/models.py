from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=120, unique=True)
    email = models.CharField(max_length=120)
    contact = models.CharField(max_length=120)
    address = models.CharField(max_length=220)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICE = (
        ('pending', 'Pending'),
        ('decline', 'Decline'),
        ('approved', 'Approved'),
        ('processing', 'Processing'),
        ('complete', 'Complete'),
    )

    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product = models.CharField(max_length=150)
    quantity = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.product

