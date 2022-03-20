from django.shortcuts import render,redirect
from django.http import HttpResponse,FileResponse
from django.contrib import messages
from .models import *
from .forms import OrderForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def orders(request):
    orders = Orders.objects.all()
    
    context = {
        'orders' : orders,
    }
    return render(request, 'orders.html', context)

@login_required
def new_order(request):
    if request.method=='POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.User = request.user
            instance.Status = '1'
            instance.save()
            messages.success(request, 'Order has been added!')
            return redirect('new_order')
    else:
        form = OrderForm()
    context = {
        'form' : form,
    }
    return render(request,'new_order.html',context)

@login_required
def clients(request):
    clients = Clients.objects.all()
    
    context = {
        'clients' : clients,
    }
    return render(request, 'clients.html', context)

@login_required
def offers(request):
   
   
    return render(request, 'offers.html')

@login_required
def other_requests(request):

    return render(request, 'other_requests.html')