from django.contrib import admin
from .models import Material , Supplier , Department , Category , District

# Register your models here.
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['name' , 'code' , 'serial' , 'quantity' , 'price' , 'category' ,'extra_expense_on' , 'expense', 'depreciation_rate' , 'supplier' ,'department' , 'district']
    list_filter = ['category', 'supplier', 'department' , 'issued' , 'district']
    list_editable = ['price' , 'quantity' , 'extra_expense_on' , 'expense', 'depreciation_rate']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display =['name' , 'slug' , 'code' , 'address1' , 'address2' ,'email', 'post_code' , 'phone_no']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display =['name' , 'slug' ,'code']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =['name' , 'slug' , 'code']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display =['name' , 'slug' , 'code' , 'email']
    prepopulated_fields = {'slug': ('name',)}
