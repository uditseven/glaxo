from django.shortcuts import render, redirect
from .models import Purchase
from .forms import PurchaseForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def base(request):
    orders = Purchase.objects.all()
    return render(request, 'base.html', {'orders': orders})

def index(request):
    if request.POST:
        form = PurchaseForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('index/', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('index/', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('index/', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = PurchaseForm()
        return render(request, 'index.html', {'form':form})