from django.test import TestCase
import requests
import datetime
# Create your tests here.
url = "http://kyandata.com/memberinfo/index"
get_rul_info = requests.get(url)
get_all_info = get_rul_info.json()['data']
print(type(get_rul_info))
print(get_all_info[1])
# a= get_all_info[1]
# d =a.get('birthday')
# d=d[0:10]
# dd=datetime.date(int(d))
# print(dd)
# a='重庆市'
# for info in get_all_info:
#     # if info.get('name')=='重庆市':

#     #     print(info.get('name'))
#     #     name = info.get('name')
#     #     name=name.replace('市','')
#     #     print(name)
#     if info.get('name')=='重庆市':
#         print(info.get('cityName'))