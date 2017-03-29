from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Widget(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class WidgetPackage(models.Model):
    PACKAGING_CHOICES = (
        ('bag', 'bag'),
        ('box', 'box'),
        ('crate', 'crate'),
    )
    widget = models.ForeignKey(Widget)
    quantity = models.IntegerField()
    packaging_type = models.CharField(choices=PACKAGING_CHOICES, max_length=10)

    def __str__(self):
        return '{} of {} {}s'.format(self.packaging_type, self.quantity, self.widget)


class InventoryItem(models.Model):
    package = models.ForeignKey(WidgetPackage)
    quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier)
    warehouse = models.ForeignKey(Warehouse)
    customer = models.ForeignKey(Customer)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return "{} - {} - {}".format(self.package, self.quantity, self.customer)
