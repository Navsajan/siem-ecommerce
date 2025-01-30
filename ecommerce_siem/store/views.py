from django.shortcuts import render
from .models import Product
import os
from django.http import JsonResponse

def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def siem_dashboard(request):
    log_file_path = 'siem.log'

    # Check if the log file exists, if not, create it
    if not os.path.exists(log_file_path):
        open(log_file_path, 'w').close()  # Create an empty file

    with open(log_file_path, 'r') as log_file:
        logs = log_file.readlines()

    return render(request, 'siem_dashboard.html', {'logs': logs})
def get_threats(request):
    data = {
        "labels": ["DDoS", "Malware", "Phishing", "Insider Threats", "Other"],
        "values": [30, 20, 15, 10, 25]
    }
    return JsonResponse(data)

def get_logs(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "values": [120, 150, 180, 220, 260, 300]
    }
    return JsonResponse(data)