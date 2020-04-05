from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'myapp'

urlpatterns = [
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),

    url(r'^item/$',
        views.ItemListView.as_view(),
        name='item_list'),

    url(r'^item/detail/(?P<pk>\d+)/$',
        views.ItemDetailView.as_view(),
        name='item_detail'),

    url(r'^item/create/$',
        views.ItemCreateView.as_view(),
        name='item_create'),

    url(r'^item/update/(?P<pk>\d+)/$',
        views.ItemUpdateView.as_view(),
        name='item_update'),

    url(r'^item/delete/(?P<pk>\d+)/$',
        views.ItemDeleteView.as_view(),
        name='item_delete'),

    url(r'^subitem/$',
        views.SubItemListView.as_view(),
        name='subitem_list'),

    url(r'^subitem/detail/(?P<pk>\d+)/$',
        views.SubItemDetailView.as_view(),
        name='subitem_detail'),

    url(r'^subitem/create/$',
        views.SubItemCreateView.as_view(),
        name='subitem_create'),

    url(r'^subitem/update/(?P<pk>\d+)/$',
        views.SubItemUpdateView.as_view(),
        name='subitem_update'),

    url(r'^subitem/delete/(?P<pk>\d+)/$',
        views.SubItemDeleteView.as_view(),
        name='subitem_delete'),
]
