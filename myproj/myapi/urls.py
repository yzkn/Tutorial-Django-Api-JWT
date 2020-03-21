from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('item', views.ItemViewSet)
router.register('subitem', views.SubItemViewSet)

app_name = 'myapi'
urlpatterns = [
    path('', include(router.urls)),
]
