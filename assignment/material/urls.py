from django.urls import path
from . import views

app_name='product'

urlpatterns=[
    path('',views.material_list , name='material_list'),
    path('<slug:category_slug>/', views.material_list , name='material_list_by_slug'),
    path('<int:id>/<slug:slug>/', views.material_detail , name='material_detail'),
]
