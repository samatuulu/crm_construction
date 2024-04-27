from django.db import models


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('reserved', 'REVERSED'),
        ('sold', 'SOLD'),
        ('installment', 'INSTALLMENT'),
        ('barter', 'BARTER'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    floor = models.IntegerField()
    object_name = models.CharField(max_length=100)
    square_meters = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.object_name} - {self.floor}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    contract_number = models.CharField(max_length=50)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
