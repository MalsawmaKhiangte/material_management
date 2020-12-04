from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order
from material.models import Category , Material
from django.http import HttpResponse
from django.template.loader import get_template
from .utils import render_to_pdf
from district.models import Aizawl, Lunglei
from decimal import Decimal
import weasyprint
from django.conf import settings


def home(request):
    form = OrderForm()
    return render(request, 'order/home.html' , {'form': form})

def order_success(request ,id):
    order = get_object_or_404(Order , id=id)
    return render(request , 'order/success.html' , {'order':order})

# AJAX
def load_materials(request):
    category_id = request.GET.get('category_id')
    materials = Material.objects.filter(category_id=category_id)
    return render(request, 'order/material_dropdown_list_options.html', {'materials': materials})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

def wait(request , id):
    order = get_object_or_404(Order , id=id)
    status1 = None
    cudis1 = None
    status2= None
    cudis2 = None
    aizawl = Aizawl.objects.all()
    lunglei = Lunglei.objects.all()
    material = Material.objects.all()
    total1 = ((order.quantity * order.material.price)+order.material.expense)
    total = (Decimal(order.material.depreciation_rate/100)*total1)
    grand_total = total1-total
    for i in aizawl:
        if (str(i.material) == str(order.material)):
            status1 = i.idle
            cudis1 = True
    for l in lunglei:
        if (str(l.material) == str(order.material)):
            status2 = l.idle
            cudis2 = True
    return render(request , 'order/invoice.html' , {'order':order , 'grand_total' : grand_total ,
                                                'status1' : status1 , 'status2' : status2 ,
                                                'cudis1' : cudis1 , 'cudis2' : cudis2})

def generate_pdf(request , id):
    order = get_object_or_404(Order , id=id)
    status1 = None
    cudis1 = None
    status2= None
    cudis2 = None
    aizawl = Aizawl.objects.all()
    lunglei = Lunglei.objects.all()
    material = Material.objects.all()
    total1 = ((order.quantity * order.material.price)+order.material.expense)
    total = (Decimal(order.material.depreciation_rate/100)*total1)
    grand_total = total1-total
    for i in aizawl:
        if (str(i.material) == str(order.material)):
            status1 = i.idle
            cudis1 = True
    for l in lunglei:
        if (str(l.material) == str(order.material)):
            status2 = l.idle
            cudis2 = True
    context = {
        'order': order ,
        'material' : material ,
        'grand_total' : grand_total ,
        'aizawl' : aizawl ,
        'lunglei' : lunglei ,
        'status1' : status1 ,
        'status2' : status2 ,
        'cudis1' : cudis1 ,
        'cudis2' : cudis2
    }

    template = get_template('order/invoice.html')
    html = template.render(context)

    pdf = render_to_pdf('order/invoice.html', {'order':order , 'grand_total' : grand_total ,
                                                'status1' : status1 , 'status2' : status2 ,
                                                'cudis1' : cudis1 , 'cudis2' : cudis2})
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" %(order.id)
        content = "inline; filename=%s" %(filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + '/css/pdf.css')])
        return response
    return HttpResponse("Not found")
