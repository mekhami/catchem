from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Supplier)
admin.site.register(models.InventoryItem)
admin.site.register(models.Warehouse)
admin.site.register(models.Widget)
admin.site.register(models.WidgetPackage)
