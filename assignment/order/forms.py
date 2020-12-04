from django import forms
from .models import Order
from material.models import Material , Category


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'district' , 'name' , 'email' ,'address' , 'category' , 'material' , 'quantity' , 'UID' , 'phone' , 'pin_code'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['material'].queryset = Material.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['material'].queryset = Material.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['material'].queryset = self.instance.category.material_set.order_by('name')
