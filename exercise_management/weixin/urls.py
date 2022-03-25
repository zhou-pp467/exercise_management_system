from django.conf.urls import url
from . import views

urlpatterns = [
    url('messages', views.Message.as_view(), name='message')
]
