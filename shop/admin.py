from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Product)
admin.site.register(models.Option)
admin.site.register(models.ProductOption)
admin.site.register(models.ProductCategory)
admin.site.register(models.Order)
admin.site.register(models.OrderDetails)
admin.site.register(models.Category)
