from django.db import models
from material.models import Material
from django.urls import reverse

DISTRICT_CHOICES = [
    ('', '--------') , ('Aizawl', 'Aizawl') , ('Lunglei' , 'Lunglei')
]

# Create your models here.
class Aizawl(models.Model):
    material = models.ForeignKey(Material , on_delete=models.CASCADE , related_name='aizawl_material' ,  null=True , blank=True )
    idle = models.BooleanField(default=False)
    send_to = models.CharField(choices=DISTRICT_CHOICES, max_length=20 , blank=True , null=True)


    def __str__(self):
        return self.material.name

    def get_absolute_url(self):
        return reverse("district:aizawl_change" , args=[self.id])

    class Meta:
        verbose_name = 'Aizawl'


class Lunglei(models.Model):
    material = models.ForeignKey(Material , on_delete=models.CASCADE , related_name='lunglei_material' ,  null=True , blank=True )
    idle = models.BooleanField(default=False)
    send_to = models.CharField(choices=DISTRICT_CHOICES, max_length=20 , blank=True , null=True)

    def __str__(self):
        return self.material.name

    def get_absolute_url(self):
        return reverse("district:lunglei_change" , args=[self.id])

    class Meta:
        verbose_name = 'Lunglei'

class quote(models.Model):
    material = models.CharField(max_length=50)
    quantity = models.CharField(max_length=10)
    For_District = models.CharField(max_length=30)
    supplier = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    Message = models.TextField(blank=True , null=True)
    created = models.DateTimeField(auto_now=True)
