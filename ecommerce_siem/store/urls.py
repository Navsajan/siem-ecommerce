from django.urls import path
from . import views
from .views import get_threats, get_logs

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('siem-dashboard/', views.siem_dashboard, name='siem-dashboard'),
    path('api/threats/', get_threats, name='get_threats'),
    path('api/logs/', get_logs, name='get_logs'),
]
