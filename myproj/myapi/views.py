from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from myapp.models import Item, SubItem
from .serializers import ItemSerializer, SubItemSerializer

from django_filters import rest_framework as filters


# API Search
class ItemFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr='contains')
    content = filters.CharFilter(field_name="content", lookup_expr='contains')
    # lookup_expr   検索方法
    # ----------------------
    # exact         完全一致
    # contains      部分一致
    # startswith    前方一致
    # endswith      後方一致
    # regex         正規表現

    order_by = filters.OrderingFilter(
        fields=(
            ('title', 'title'),  # (カラム名,パラメータ名)
            ('content', 'text'),
        ),
    )

    class Meta:
        model = Item
        fields = ['title', 'content']


# ViewSets

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]
    filter_class = ItemFilter


class SubItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SubItem.objects.all()
    serializer_class = SubItemSerializer
    permission_classes = [IsAuthenticated]
