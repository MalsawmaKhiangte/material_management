from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=30 , unique=True)

    class Meta:
        ordering = ('-name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=30 , unique=True)
    address1 = models.TextField()
    address2 = models.TextField()
    post_code = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=10 ,unique=True)
    email = models.EmailField(max_length=100 , default='exampl@email.com')

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=30 , unique=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=30 , unique=True)
    email = models.EmailField(max_length=30 , blank=True , null=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    code = models.CharField(max_length=30 , unique=True)
    image = models.ImageField(upload_to='materials/%Y/%m/%d' , blank=True)
    serial = models.CharField(max_length=30 , unique=True)
    quantity = models.IntegerField(blank=True , null=True)
    price = models.DecimalField(max_digits=7 , decimal_places=2)
    extra_expense_on = models.CharField(max_length=80 , blank=True , null=True)
    expense = models.DecimalField( max_digits=10 , decimal_places=2 , blank=True , null=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='item_category')
    supplier = models.ForeignKey(Supplier , on_delete=models.CASCADE , related_name='item_supplier')
    department = models.ForeignKey(Department , on_delete=models.CASCADE , related_name='item_dept' , null=True , blank=True)
    district = models.ForeignKey(District , on_delete=models.CASCADE , related_name='item_dept' , null=True , blank=True)
    depreciation_rate = models.IntegerField(blank=True , null=True)
    reparing = models.BooleanField(default=False)
    working = models.BooleanField(default=False)
    issued = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-name',)

    def __str__(self):
        return self.name
