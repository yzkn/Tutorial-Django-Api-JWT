from django.shortcuts import render

from rest_framework import viewsets

from myapp.models import Item, SubItem

from .serializers import ItemSerializer, SubItemSerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class SubItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubItem.objects.all()
    serializer_class = SubItemSerializer
