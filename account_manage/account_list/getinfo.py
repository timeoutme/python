
import requests
# import account_list.models


url = "http://kyandata.com/memberinfo/index"
get_rul_info = requests.get(url)
get_rul_info = get_rul_info.json()['data']
# print(type(get_rul_info))
# print(get_rul_info)
print(get_rul_info[1])
a=0
# for info in get_rul_info:
#     # print (info['logName'])
#     a+=1
#     print(a)
#     print(info['name'])

# account_info = Accounts(account=info['logName'],area=info['country'],province=info['name'],city=info['cityName'],sex=info['sex'],
#                 birthday=info['birthday'],edu=info['education'],trade=trade,position=info['job'],marriage=info['maritalStatus'],
#                 working=working,child=child,user=info['owerName'],zip_code=info['zip'],age=year,child_age=child_year,child_birthday=child_birthday,
#                 personal_monthly_income=personal_monthly_income,family_monthly_income=family_monthly_income)
# account_info.save()