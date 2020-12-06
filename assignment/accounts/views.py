from django.shortcuts import render ,get_object_or_404 , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login
from .forms import LoginForm , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from order.models import Order
from order.filters import OrderFilter
from material.models import Material
from accounts.models import Profile
from django.contrib.auth.models import User
from decimal import Decimal
from district.models import Aizawl, Lunglei

@login_required
def difviews(request):
    order = Order.objects.all().order_by('-created')
    material = Material.objects.all()
    profile = Profile(request)
    myFilter = OrderFilter(request.GET , queryset=order)
    order = myFilter.qs
    if request.user.is_authenticated:
        if request.user.profile.designation=="Purchase Manager":
            return render(request , 'accounts/pm.html' , {'order':order , 'material':material , 'myFilter':myFilter})
        elif request.user.profile.designation=="District Manager":
            if request.user.profile.city=="Aizawl":
                return redirect('district:aizawl_view')
            elif request.user.profile.city=="Lunglei":
                return redirect('district:lunglei_view')
            else:
                return redirect('logout')
    else:
        return redirect('logout')


@login_required
def order_detail(request , id):
    status1 = None
    cudis1 = None
    status2= None
    cudis2 = None
    aizawl = Aizawl.objects.all()
    lunglei = Lunglei.objects.all()
    material = Material.objects.all()
    order = get_object_or_404(Order, id=id)
    if (str(order.district) != str(order.material.district)):
        line = True
    else:
        line = False
    total1 = ((order.quantity * order.material.price)+order.material.expense)
    total = (Decimal(order.material.depreciation_rate/100)*total1)
    grand_total = total1-total

    if (order.quantity <= order.material.quantity):
        less = True
    else:
        less = False

    for i in aizawl:
        if (str(i.material) == str(order.material)):
            status1 = i.idle
            cudis1 = True
    for l in lunglei:
        if (str(l.material) == str(order.material)):
            status2 = l.idle
            cudis2 = True
    return render(request , 'accounts/detail.html', {'order':order ,
                                                    'material':material ,
                                                    'grand_total':grand_total ,
                                                    'less':less,
                                                    'aizawl':aizawl ,  'lunglei':lunglei , 'line':line, 'status1':status1,
                                                    'cudis1':cudis1 , 'status2':status2,
                                                    'cudis2':cudis2})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request , username=cd['username'] , password=cd['password'])
            if user is not None:
                if user.is_active():
                    login(request, user)
                    return HttpResponse('Authenticate')
                else:
                    return HttpResponse('Diabled ac')
            else:
                return HttpResponse('Invalid Login')
    else:
        form = LoginForm()
    return render(request , 'accounts/login.html' , {'form':form})

def register(request):
    if request.method =='POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user , designation=cd['designation'] , city=cd['city'])
            return render(request, 'accounts/register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html',{'user_form':user_form})
