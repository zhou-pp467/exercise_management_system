from django.shortcuts import render
from rest_framework.views import APIView
from wechatpy.utils import check_signature
from wechatpy import parse_message, create_reply
from wechatpy.exceptions import InvalidSignatureException


class Message(APIView):
    def get(self, request):



