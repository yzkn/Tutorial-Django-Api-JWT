from rest_framework import serializers

from myapp.models import Item, SubItem


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('title', 'content')

# サブリストシリアライザ


class SubItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubItem
        fields = ('item', 'subtitle', 'subcontent')
