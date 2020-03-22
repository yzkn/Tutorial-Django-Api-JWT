from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Item, SubItem
from .forms import ItemForm, SubItemForm

from django.contrib.auth.mixins import LoginRequiredMixin  # UserAuth
from django.contrib.auth.models import User


class ItemListView(ListView):
    """
    GET(全件)
    templates\myapp\モデル_list.htmlを使用
    """
    model = Item
    paginate_by = 10  # ページネーション(10件ごとに表示)


class ItemDetailView(LoginRequiredMixin, DetailView):
    """
    GET(a record)
    templates\myapp\モデル_detail.htmlを使用
    """
    model = Item


class ItemCreateView(LoginRequiredMixin, CreateView):
    """
    POST用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('myapp:item_list')

    def form_valid(self, form):
        result = super().form_valid(form)
        messages.success(
            self.request, 'Created: {}'.format(form.instance))
        return result

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        result = super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    PUT用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = Item
    form_class = ItemForm

    success_url = reverse_lazy('myapp:item_list')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        result = super().form_valid(form)
        messages.success(
            self.request, 'Updated: {}'.format(form.instance))
        return result


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    """
    DELETE用画面
    templates\myapp\モデル_confirm_delete.htmlを使用
    """
    model = Item
    form_class = ItemForm

    success_url = reverse_lazy('myapp:item_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Removed: {}'.format(self.object))
        return result
