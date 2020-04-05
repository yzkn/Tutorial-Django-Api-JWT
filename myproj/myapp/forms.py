from django import forms

from .models import Item, SubItem


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'content']


class ItemSearchForm(forms.Form):
    title = forms.CharField(
        initial='',
        label='Title',
        required=False,
    )
    content = forms.CharField(
        initial='',
        label='Content',
        required=False,
    )


class SubItemForm(forms.ModelForm):
    class Meta:
        model = SubItem
        fields = ['item', 'subtitle', 'subcontent']
