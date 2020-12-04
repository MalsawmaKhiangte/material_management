from django.shortcuts import render, HttpResponseRedirect ,redirect , get_object_or_404
from django.urls import reverse
from district.forms import quoteForm , reqForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from district.models import quote
from order.models import Order
from order.forms import OrderForm

# Create your views here.
def sendquote(request , id):
    order = get_object_or_404(Order , id =id)
    form = quoteForm()
    if request.method == 'POST':
        form = quoteForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Request of material ' + cd['material'] + ' for ' + cd['For_District']
            message = cd['Message']
            recipient = cd['email']
            send_mail(subject , message , settings.EMAIL_HOST_USER , [recipient] , fail_silently=False)
            quote.objects.create(material=cd['material'] , quantity=cd['quantity'] , For_District=cd['For_District'] , supplier=cd['supplier'] , address=cd['address'] , email=recipient , Message=message)
            messages.success(request , "order successfull")
            order.complete = True
            order.save()
            return render(request , 'district/quote.html', {'form':form , 'order':order})
    else:
        form = quoteForm()
    return render(request , 'district/quote.html', {'form':form})

def sendmaterial(request, id):
    order = get_object_or_404(Order , id =id)
    form = reqForm()
    if request.method == 'POST':
        form = reqForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = 'Request of material ' + str(order.material) + ' for ' +  str(order.district)
            recipient = order.material.district.email
            message = cd['message']
            send_mail(subject , message , settings.EMAIL_HOST_USER , [recipient] , fail_silently=False)
            messages.success(request , "successfully request to sent materials")
            return redirect('difviews')
    else:
        form = reqForm()
    return render(request , 'district/reqdis.html', {'form':form , 'order':order})

def ordermail(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = Order.objects.create(name=cd['name'] , address=cd['address'] , category =cd['category'] ,
                                        material=cd['material'] , quantity=cd['quantity'] , UID = cd['UID'] ,
                                        district=cd['district'] , phone = cd['phone'],
                                        email = cd['email'] , pin_code = cd['pin_code'])
            order.save()
            subject = 'Thank you ' + cd['name'] + ' for registering'
            recipient = cd['email']
            message = 'This email will be used for giving information'
            send_mail(subject , message , settings.EMAIL_HOST_USER , [recipient] , fail_silently=False)
            return redirect('order:waiting' , id=order.id)
    else:
        form = OrderForm()
    return redirect('order:home')
