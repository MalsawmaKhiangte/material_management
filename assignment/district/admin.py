from django.contrib import admin
from .models import Aizawl , Lunglei , quote

@admin.register(Aizawl)
class AizawlAdmin(admin.ModelAdmin):
    list_display =['material' , 'idle',]
    list_editable = ['idle']

@admin.register(Lunglei)
class LungleiAdmin(admin.ModelAdmin):
    list_display =['material' , 'idle']
    list_editable = ['idle']

@admin.register(quote)
class quoteAdmin(admin.ModelAdmin):
    list_display =['material' , 'quantity' , 'For_District' , 'supplier' , 'address' , 'email' , 'Message' , 'created']
