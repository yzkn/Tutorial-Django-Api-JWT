from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .models import Item, SubItem
from .forms import ItemForm, ItemSearchForm, SubItemForm

from django.contrib.auth.mixins import LoginRequiredMixin  # UserAuth
from django.contrib.auth.models import User

from django.db.models import Q
from functools import reduce
from operator import and_


class IndexView(TemplateView):
    template_name = 'myapp/index.html'


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
        form.instance.author_id = self.request.user.id
        result = super().form_valid(form)
        messages.success(
            self.request, 'Created: {}'.format(form.instance))
        return result


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


class ItemSearchView(LoginRequiredMixin, ListView):
    paginate_by = 10
    template_name = 'myapp/item_search.html'
    model = Item

    def post(self, request, *args, **kwargs):
        form_value = [
            self.request.POST.get('title', None),
            self.request.POST.get('content', None),
        ]
        request.session['form_value'] = form_value
        self.request.GET = self.request.GET.copy()
        self.request.GET.clear()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = ''
        content = ''
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            content = form_value[1]
        default_data = {'title': title,
                        'content': content,
                        }
        item_search_form = ItemSearchForm(initial=default_data)
        context['item_search_form'] = item_search_form
        return context

    def get_queryset(self):
        if 'form_value' in self.request.session:
            form_value = self.request.session['form_value']
            title = form_value[0]
            content = form_value[1]
            condition_title = Q()
            condition_content = Q()
            if len(title) != 0 and title[0]:
                condition_title = reduce(
                    and_, [Q(title__icontains=title_word) for title_word in title.split()])
            if len(content) != 0 and content[0]:
                condition_content = reduce(
                    and_, [Q(content__icontains=content_word)
                           for content_word in content.split()]
                )
            return Item.objects.select_related().filter(condition_title & condition_content)
        else:
            return Item.objects.none()


class SubItemListView(ListView):
    """
    GET(全件)
    templates\myapp\モデル_list.htmlを使用
    """
    model = SubItem
    paginate_by = 10  # ページネーション(10件ごとに表示)


class SubItemDetailView(LoginRequiredMixin, DetailView):
    """
    GET(a record)
    templates\myapp\モデル_detail.htmlを使用
    """
    model = SubItem


class SubItemCreateView(LoginRequiredMixin, CreateView):
    """
    POST用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = SubItem
    form_class = SubItemForm
    success_url = reverse_lazy('myapp:subitem_list')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        result = super().form_valid(form)
        messages.success(
            self.request, 'Created: {}'.format(form.instance))
        return result


class SubItemUpdateView(LoginRequiredMixin, UpdateView):
    """
    PUT用画面
    templates\myapp\モデル_form.htmlを使用
    """
    model = SubItem
    form_class = SubItemForm

    success_url = reverse_lazy('myapp:subitem_list')

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        result = super().form_valid(form)
        messages.success(
            self.request, 'Updated: {}'.format(form.instance))
        return result


class SubItemDeleteView(LoginRequiredMixin, DeleteView):
    """
    DELETE用画面
    templates\myapp\モデル_confirm_delete.htmlを使用
    """
    model = SubItem
    form_class = SubItemForm

    success_url = reverse_lazy('myapp:subitem_list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        messages.success(
            self.request, 'Removed: {}'.format(self.object))
        return result
