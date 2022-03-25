from django.conf.urls import url
from weixin.views import message

urlpatterns = [
    url('', message)
]
