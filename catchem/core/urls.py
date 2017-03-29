from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.InventoryItemList.as_view(), name='index'),
    url(r'^create/$', views.InventoryItemCreate.as_view(), name='create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.InventoryItemDetail.as_view(), name='detail'),
]
