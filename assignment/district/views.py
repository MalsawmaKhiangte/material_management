from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Aizawl , Lunglei
from django.urls import reverse
from material.models import Material
from order.models import Order
from .forms import quoteForm , reqForm , AdisChoices , LdisChoices
from django.contrib import messages

def aizawl_view(request):
    aizawl = Aizawl.objects.all()
    forms = AdisChoices()
    return render(request , 'district/dm.html', {'aizawl':aizawl , 'forms':forms ,})

def lunglei_view(request):
    lunglei = Lunglei.objects.all()
    forms = LdisChoices()
    return render(request , 'district/dm2.html', {'lunglei':lunglei, 'forms':forms})

def aizawl_change(request, id):
    aizawl = get_object_or_404(Aizawl , id=id)
    aizawl.idle ^= True
    aizawl.save()
    return redirect('district:aizawl_view')


def lunglei_change(request , id):
    lunglei = get_object_or_404(Lunglei , id=id)
    lunglei.idle = not lunglei.idle
    lunglei.save()
    return redirect('district:lunglei_view')

def quote(request , id , district):
    aizawl = Aizawl.objects.all()
    lunglei = Lunglei.objects.all()
    material = Material.objects.all()
    order = get_object_or_404(Order, id=id , district=district)
    data = {'material':order.material , 'quantity':order.quantity , 'For_District':order.district , 'supplier':order.material.supplier , 'address':order.material.supplier.address1 , 'email':order.material.supplier.email}
    form = quoteForm(initial=data)

    return render(request , 'district/quote.html' , {'order':order ,
                                                    'material':material ,
                                                    'aizawl':aizawl ,  'lunglei':lunglei , 'form':form})

def allocateaizawl(request , id):
    order = get_object_or_404(Order, id=id)
    if order.district == 'Aizawl':
        aizawl = Aizawl.objects.create(material=order.material)
        aizawl.save()
    else:
        lunglei = Lunglei.objects.create(material = order.material)
        lunglei.save()
    order.complete=True
    order.save()
    messages.success(request , "allocated to " + str(order.district))
    return redirect('difviews')

def reqDis(request , id):
    order = get_object_or_404(Order, id=id)
    data = {'to_district':order.district , 'req_material':order.material}
    form = reqForm(initial=data)
    return render(request , 'district/reqdis.html' , {'order':order ,
                                                     'form':form})

def dis_change(request, id):
    item = get_object_or_404(Lunglei , id=id)
    if item.send_to == 'Aizawl':
        aizawl = Aizawl.objects.create(material = item.material)
        aizawl.save()
    item.delete()
    return redirect('district:lunglei_view')

def dis_change_azl(request, id):
    item = get_object_or_404(Aizawl , id=id)
    if item.send_to == 'Lunglei':
        lunglei = Lunglei.objects.create(material = item.material)
        lunglei.save()
    item.delete()
    return redirect('district:aizawl_view')
