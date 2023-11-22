from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales_manager_panel, name='sales_manger')
]