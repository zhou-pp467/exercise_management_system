from django.shortcuts import render
from wechatpy.utils import check_signature
from wechatpy import parse_message, create_reply
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.replies import TextReply
from rest_framework.decorators import api_view
import hashlib
from django.http import HttpResponse
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

from serializers import StrengthRecordSerializer, RunningRecordSerializer,\
    ExercisePlanSerializer,RunningPlanSerializer
from exercise_type.models import StrengthTrainingRecord
from plan.models import ExercisePlanItem, RunningPlanItem
from running.models import RunningRecord


token = "exercisemanagementsystem"


def get_week():
    day_list = []
    today = datetime.today()
    monday = today
    while monday.weekday() != 0:
        monday = monday - timedelta(days=1)
    for i in range(7):
        day_list.append(monday + timedelta(days=i))
    return day_list


def get_day_data(date):
    running_records = RunningRecord.objects.filter(date=date)
    strength_training_records = StrengthTrainingRecord.objects.filter(date=date)
    exercise_plan_items = ExercisePlanItem.objects.filter(date=date)
    running_plan_items = RunningPlanItem.objects.filter(date=date)
    strength_records_serializer = StrengthRecordSerializer(strength_training_records, many=True)
    running_records_serializer = RunningRecordSerializer(running_records, many=True)
    exercise_plan_serializer = ExercisePlanSerializer(exercise_plan_items, many=True)
    running_plan_serializer = RunningPlanSerializer(running_plan_items, many=True)

    return f"""
    计划锻炼项目：{('，'.join([i['type'] for i in exercise_plan_serializer.data]))}\
{'，' if (exercise_plan_serializer.data and running_plan_serializer.data) else ''}\
{'跑步' if running_plan_serializer.data else ''}
    完成锻炼项目：{('，'.join([i['type'] for i in strength_records_serializer.data]))}\
{'，' if (strength_records_serializer.data and running_records_serializer.data) else ''}\
{'跑步' if running_records_serializer.data else ''}
    """


@api_view(['GET', 'POST'])
def message(request):
    if request.method == 'GET':
        try:
            signature = request.GET.get('signature')
            timestamp = request.GET.get('timestamp')
            nonce = request.GET.get('nonce')
            echostr = request.GET.get('echostr')

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            sha1.update(list[0].encode("utf-8"))
            sha1.update(list[1].encode("utf-8"))
            sha1.update(list[2].encode("utf-8"))
            hashcode = sha1.hexdigest()  # 获取加密串
            print("handle/GET func: hashcode, signature: ", hashcode, signature)

            if hashcode == signature:
                return HttpResponse(echostr)
            else:
                return HttpResponse('')
        except Exception:
            return HttpResponse(f'{Exception}')

    if request.method == 'POST':
        reply_content = '请输入“今日计划”获取当日计划，或者输入“本周计划”获取本周计划及执行情况'
        msg = parse_message(request.body)
        xmlData = ET.fromstring(request.body)
        content = xmlData.find('Content').text
        reply = TextReply(message=msg)
        if content == '今日计划':
            date = datetime.today()
            reply_content = f'今日计划：{get_day_data(date)}'
        if content == '本周计划':
            num_list = ['一', '二', '三', '四', '五', '六', '日']
            reply_content = f'本周计划：\n    '
            days = get_week()
            for i, day in enumerate(days):
                reply_content += f'周{num_list[i]}{get_day_data(day)}'
        reply.content = reply_content
        response = HttpResponse(reply.render(), content_type="application/xml")
        return response

