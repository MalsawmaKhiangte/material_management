from django.urls import path
from . import views

app_name = 'district'

urlpatterns = [
    path('aizawl_view/',views.aizawl_view , name="aizawl_view"),
    path('lunglei_view/',views.lunglei_view , name="lunglei_view"),
    path('<int:id>/',views.lunglei_change , name='lunglei_change'),
    path('aizawl/<int:id>/',views.aizawl_change , name='aizawl_change'),
    path('quote/<int:id>/<str:district>/', views.quote , name='quote'),
    path('allocateaizawl/<int:id>/', views.allocateaizawl , name='allocateaizawl'),
    path('reqdis/<int:id>/', views.reqDis , name='reqDis'),
    path('dis_change/<int:id>/',views.dis_change , name='dis_change'),
    path('dis_change_azl/<int:id>/',views.dis_change_azl, name='dis_change_azl'),
]
