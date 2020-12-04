from django.db import models
from django.urls import reverse
from material.models import Material , Category
from decimal import Decimal

DISTRICT_CHOICE = [
    ('Aizawl' , 'Aizawl') , ('Lunglei' , 'Lunglei')
]


class Order(models.Model):
    district =models.CharField(choices=DISTRICT_CHOICE , max_length=10)
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, blank=True , null=True)
    material = models.ForeignKey(Material , on_delete=models.CASCADE, blank=True , null=True)
    quantity = models.IntegerField(blank=True)
    UID = models.IntegerField()
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    pin_code = models.CharField(max_length=20)
    created =models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)


    class Meta:
        ordering =('-created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_absolute_url(self):
        return reverse('order_detail' , args=[self.id])
