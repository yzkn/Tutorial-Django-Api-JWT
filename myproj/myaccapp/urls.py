from . import views
from django.urls import path


app_name = 'myaccapp'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
