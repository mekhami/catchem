from django.views.generic import ListView, DetailView, UpdateView, CreateView

from . import models
from .forms import InventoryItemForm


# Create your views here.
class InventoryItemList(ListView):
    model = models.InventoryItem


class InventoryItemDetail(DetailView):
    model = models.InventoryItem


class InventoryItemUpdate(UpdateView):
    model = models.InventoryItem
    form_class = InventoryItemForm


class InventoryItemCreate(CreateView):
    model = models.InventoryItem
    form_class = InventoryItemForm
