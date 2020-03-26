from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    title = models.CharField(
        verbose_name='タイトル',
        max_length=200,
        default='',
        blank=True)
    content = models.TextField(
        verbose_name='本文',
        default='',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='id')

    def __str__(self):
        return self.title


class SubItem(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.PROTECT, related_name='subitem')
    subtitle = models.CharField(
        verbose_name='サブタイトル',
        max_length=200,
        default='',
        blank=True)
    subcontent = models.TextField(
        verbose_name='サブ本文',
        default='',
        blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name='id')

    def __str__(self):
        return self.subtitle


def create_default_user(sender, **kwargs):
    for i in range(5):
        User.objects.get_or_create(
            email='y{}@example.net'.format(i),
            username='U{}'.format(i)
        )
        u = User.objects.get(username__exact='U{}'.format(i))
        u.set_password('Passw0rd!')
        u.save()


def create_default_item(sender, **kwargs):
    for i in range(5):
        Item.objects.get_or_create(
            author=User.objects.filter(
                username='U{}'.format(i)).first(),
            content='C{}'.format(i),
            title='T{}'.format(i)
        )


def create_default_subitem(sender, **kwargs):
    for i in range(5):
        SubItem.objects.get_or_create(
            author=User.objects.filter(
                username='U{}'.format(i)).first(),
            subcontent='C{}'.format(i),
            subtitle='T{}'.format(i),
            item_id=Item.objects.filter(title='T{}'.format(i)).first().pk
        )
