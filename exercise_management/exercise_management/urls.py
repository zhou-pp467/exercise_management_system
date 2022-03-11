"""exercise_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from plan.views import get_calendar_data, get_day_data


admin.site.site_header = "周雷的运动管理后台"
admin.site.site_title = "运动记录"
admin.site.index_title = "周雷的运动管理后台"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_calendar_data', get_calendar_data, name='get_calendar_data'),
    path('get_day_data', get_day_data, name='get_day_data')
]
