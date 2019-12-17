import requests


url = "http://kyandata.com/memberinfo/index"
get_rul_info = requests.get(url)
get_rul_info = get_rul_info.json()['data']
print(type(get_rul_info))
print(get_rul_info)