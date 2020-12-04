from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'address' , 'quantity' , 'UID' , 'district' , 'phone' ,'email' , 'pin_code', 'created' , 'complete']
    list_filter = ['complete' , 'district']

# Register your models here.
