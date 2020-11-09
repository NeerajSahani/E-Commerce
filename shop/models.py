from django.db import models
from .validators import phone_validator
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='category/thumbnail', blank=True)

    def __str__(self):
        return self.name


class Option(models.Model):
    option_name = models.CharField(max_length=100)

    def __str__(self):
        return self.option_name


class Product(models.Model):
    sku = models.BigIntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnail', blank=True)
    image = models.ImageField(upload_to='products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True)
    stock = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    option = models.ForeignKey(Option, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product.name + ' - ' + self.option.option_name


class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


class Customer(User):
    billing_address = models.TextField()
    default_shipping_address = models.TextField()
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=False)

    def __str__(self):
        return self.get_full_name()


class Order(models.Model):
    ORDER_STATUS = [
        ('Confirmed', 'Confirmed'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2)
    shipping_address = models.TextField()
    order_address = models.TextField()
    order_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Confirmed')


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(decimal_places=2)
    sku = models.BigIntegerField()
    quantity = models.IntegerField(default=1)
