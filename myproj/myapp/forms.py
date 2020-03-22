from django import forms

from .models import Item, SubItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['author', 'title', 'content']


class SubItemForm(forms.ModelForm):
    class Meta:
        model = SubItem
        fields = ['author', 'subtitle', 'subcontent']
