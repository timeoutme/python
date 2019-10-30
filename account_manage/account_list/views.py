from django.shortcuts import render,redirect
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
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

    # if request.method == 'POST':
    area = request.GET.get('area')
    province = request.GET.get('province')
    city = request.GET.get('city')
    county = request.GET.get('county')
    

    search_dict = dict()

    if area:
        search_dict['area'] = area
    if province:
        search_dict['province'] = province
    if city:
        search_dict['city'] = city
    if county:
        search_dict['county'] = county

    search_of_list = Accounts.objects.filter(**search_dict)  
    
    pageing = Paginator(search_of_list,10) 
    page_num = request.GET.get('page',1)
    page_list = pageing.get_page(page_num)
    

    page_data =dict()
    page_data['page_list'] = page_list
    page_data['pages'] = page_list.object_list
    page_data['area'] = area
    page_data['province'] =province
    page_data['city'] = city
    page_data['county'] = county
    
    

    return render(request,'search_list.html',page_data)
    