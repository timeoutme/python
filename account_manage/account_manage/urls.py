"""account_manage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from account_list.views import home, add, add_save, login, search, register, logoutt, delete, hide, get_info, cler_info, quc, search_userid

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='主页'),
    path('add/',add,name='添加'),
    path('add/save/',add_save,name='保存'),
    path('login/',login,name='登录'),
    path('search_userid/', search_userid, name='搜索ID'),
    path('search/',search, name='搜索'),
    path('register/',register,name='注册'),
    path('logout',logoutt,name='退出'),
    path('delete/<ss_id>',delete,name='删除'),
    path('hide/<ss_id>',hide,name='隐藏'),
    path('get_info',get_info,name='获取信息'),
    path('cler_info',cler_info,name='清除数据'),
    path('quc',quc,name='去除重复')
]
