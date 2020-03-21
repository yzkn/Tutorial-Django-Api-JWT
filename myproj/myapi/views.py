from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from myapp.models import Item, SubItem
from .serializers import ItemSerializer, SubItemSerializer


class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]


class SubItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubItem.objects.all()
    serializer_class = SubItemSerializer
    permission_classes = [IsAuthenticated]
