from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('' , views.home , name='home'),
    #path('order_create/', views.order_create, name='order_create'),
    path('ajax/load-materials/', views.load_materials, name='ajax_load_materials'), # AJAX
    path('order_success/<int:id>/' , views.order_success , name='order_success'),
    path('waiting/<int:id>', views.wait, name='waiting'),
    path('pdf/<int:id>/', views.generate_pdf , name='pdf'),
]
