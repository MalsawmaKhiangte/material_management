from django.urls import path
from . import views

app_name = 'sendmail'

urlpatterns = [
    path('send/<int:id>/',views.sendquote , name='send'),
    path('sendmaterial/<int:id>/', views.sendmaterial , name='sendmaterial'),
    path('ordermail/',views.ordermail , name='ordermail')
]
