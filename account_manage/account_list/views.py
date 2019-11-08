from django.shortcuts import render,redirect
from .models import Accounts,User_account
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
import datetime
# Create your views here.

@login_required
def home(request):
    
    user = request.user
    display_all = Accounts.objects.filter(user=user)
    display_page = Paginator(display_all,10)
    page_num = request.GET.get('page',1)
    page_list = display_page.get_page(page_num)
    current_page = page_list.number
    pages = display_page.num_pages    
    page_of_pages = display_page.page_range

    page_data =dict()
    page_data['page_list'] = page_list
    page_data['page'] = page_list.object_list

    return render(request,'display_list.html',page_data)
    
    # return render(request,'home.html',{'账号':Accounts.objects.all()})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')   
    elif request.method == 'POST':
               
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect('主页') 
        else:
            return render(request,'login.html', {'错误':'用户名或密码错误'})
    

        # username = request.POST['用户名']
        # password = request.POST['密码']
        # user = auth.authenticate(username=user_name,password=password1)
        # if user is None:
        #     return render(request,'login.html', {'错误':'用户名或密码错误'})
        # else:
        #     auth.login(request,user)
        #     return redirect('主页')


def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')
            
            if not all([username,password,password1]):
                
                return render(request,'register.html',{'值为空':'用户名或密码不能为空'})
            db_username = User.objects.filter(username__exact=username)
            if db_username:
                return render(request,'register.html',{'用户名错误':'您输入的用户名已被占用，请重新输入！'})        

            if password == password1:
                
                User.objects.create_user(username=username,password=password1)
                
                return redirect('登录')
            else:
                return render(request,'register.html',{'密码错误':'您输入的密码不一致，请重新输入！'})

        # username = request.POST.get('username',None)
        # password = request.POST.get('password',None)
        # password1 = request.POST.get('password1',None)   
        # if password==password1:
        #     password=password1
        # else:
        #     return render(request,'register.html',{'密码错误':'您输入的密码不一致，请重新输入！'})
        # try:
        #     user = User.objects.get(username=username)    
        # except Exception:
        #     user = None
        # if user:    
        #     return render(request,'register.html',{'用户名错误':'您输入的用户名已被占用，请重新输入！'})
        
        # User.objects.create_user(username=username,password=password)
        # return redirect('登录')
        
        


def logoutt(request):
    auth.logout(request)
    return redirect('登录')



def add(request):
    return render(request,'add.html')   

def add_save(request):
    if request.method == 'POST':
        if request.POST['account'] and request.POST.get('province'):
            account = request.POST['account']            
            area = request.POST['area']
            province = request.POST.get('province')
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
            
            acc = Accounts(account=account,area=area,province=province,city=city,county=county,sex=sex,
                birthday=birthday,edu=edu,trade=trade,position=position,marriage=marriage,working=working,child=child,user=user,zip_code=zip_code,age=year)
            acc.save()
            return render(request,'add.html',{'成功':'添加成功'})
        else:
            return render(request,'add.html',{'错误':'添加失败，请填写省份地区信息'})    
    elif request.method == 'GET':
        return render(request,'add.html')





def search(request): 

    # if request.method == 'POST':
    area = request.GET.get('area')
    province = request.GET.get('province')
    city = request.GET.get('city')
    county = request.GET.get('county')
    user = request.user

    search_dict = dict()

    if area:
        search_dict['area'] = area
    if province:
        search_dict['province'] = province
    if city:
        search_dict['city'] = city
    if county:
        search_dict['county'] = county

    search_of_list = Accounts.objects.filter(user=user,**search_dict)  
    
    pageing = Paginator(search_of_list,10) 
    page_num = request.GET.get('page',1)
    page_list = pageing.get_page(page_num)
    current_page = page_list.number
    pages = pageing.num_pages    
    page_of_pages = pageing.page_range

    page_data =dict()
    page_data['page_list'] = page_list
    page_data['page'] = page_list.object_list
    page_data['area'] = area
    page_data['province'] =province
    page_data['city'] = city
    
    
    # age = now_year - int(Accounts.age[0])
    # page_data['age'] = age
    page_data['county'] = county
    page_data['page_of_pages'] = page_of_pages
    page_data['current_page'] = current_page

    
    

    return render(request,'search_list.html',page_data)