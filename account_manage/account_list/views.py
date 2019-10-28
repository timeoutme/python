from django.shortcuts import render,redirect
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib import auth
from django.db.models import Q
# Create your views here.

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')   
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        password1 = request.POST['密码']
        user = auth.authenticate(username=user_name,password=password1)
        if user is None:
            return render(request,'login.html', {'错误':'用户名或密码错误'})
        else:
            auth.login(request,user)
            return redirect('主页')




def add(request):
    return render(request,'add.html')   

def add_save(request):
    if request.method == 'POST':
        if request.POST['account']:
            account = request.POST['account']
            print(account)
            area = request.POST['area']
            province = request.POST['province']
            city = request.POST['city']
            county = request.POST['county']
            sex = request.POST['sex']         
            edu = request.POST['edu']
            trade = request.POST['trade']
            position = request.POST['position']
            marriage = request.POST['marriage']
            working = request.POST['working']
            child = request.POST['child']
            zip_code = request.POST['zip_code']  
            user = request.user

            year = request.POST['year']
            month = request.POST['month']
            day = request.POST['day']
            birthday = year + '年' + month + '月' + day + '日'

            acc = Accounts(account=account,area=area,province=province,city=city,county=county,sex=sex,birthday=birthday,edu=edu,trade=trade,position=position,marriage=marriage,working=working,child=child,user=user,zip_code=zip_code)
            acc.save()
            return render(request,'add.html',{'账号':Accounts.objects.all()})
        else:
            return render(request,'add.html',{'错误':'请查看是否有信息没填','账号':Accounts.objects.all()})    
    elif request.method == 'GET':
        return render(request,'add.html',{'账号':Accounts.objects.all()})


def home(request):
    return render(request,'home.html',{'账号':Accounts.objects.all()})


def search(request):
    if request.method == 'POST':
        area = request.POST.get('area')
        province = request.POST.get('province')
        city = request.POST.get('city')
        county = request.POST.get('county')
        area_list = Accounts.objects.filter(area=area)
        province_list = Accounts.objects.filter(area=area,province=province)
        city_list = Accounts.objects.filter(area=area,province=province,city=city)
        county_list = Accounts.objects.filter(area=area,province=province,city=city,county=county)
        # search_get_list = Accounts.objects.filter(Q(area__startswith=area) | Q(province__startswith=province) | Q(city__startswith=city) & Q(county__startswith=county))
        if area:
            if province:
                
                if city:

                    if county:
                        return render(request,'search_list.html',{'搜索列表':county_list})
                    else:
                        return render(request,'search_list.html',{'搜索列表':city_list})   
                else:
                    return render(request,'search_list.html',{'搜索列表':province_list})
            else:
                return render(request,'search_list.html',{'搜索列表':area_list})    
       
       
        

        