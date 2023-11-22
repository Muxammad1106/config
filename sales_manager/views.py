from django.shortcuts import render, redirect
from .models import Lead


# Create your views here.


def sales_manager_panel(request):
    return render(request, 'sales_manager_panel.html')


def sales_manger(request):
    leads = Lead.objects.all()
    context = {'leads': leads}
    return render(request, 'sales_manager_panel.html', context)


def add_lead(request):
    if request.method == 'POST':
        name = request.POST['name']
        office_visited = 'office_visited' in request.POST
        contract_signed = 'contract_signed' in request.POST
        phone_number = request.POST['phone_number']
        sales_channel = request.POST['sales_channel']
        description = request.POST['description']
        Lead.objects.create(
            name=name,
            office_visited=office_visited,
            contract_signed=contract_signed,
            phone_number=phone_number,
            sales_channel=sales_channel,
            description=description
        )
        return redirect('home')

    return render(request, 'sales_manager_panel.html')


def sales_manager_info(request):
    leads = [
        {'name': 'Lead 1', 'phone_number': '1234567890'},
        {'name': 'Lead 2', 'phone_number': '9876543210'},
    ]
    manager_info = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'phone': '555-1234',
    }
    context = {
        'leads': leads,
        'manager_info': manager_info,
    }
    return render(request, 'sales_manager_panel.html', context)