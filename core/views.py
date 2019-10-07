from django.shortcuts import render, redirect
from .models import Purchase
<<<<<<< HEAD
from .forms import PurchaseForm
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
=======
from .models import Medicine
>>>>>>> 67d417ebeb68daf6033828affe4db63efb8e6c65
# Create your views here.

def base(request):
    orders = Purchase.objects.all()
<<<<<<< HEAD
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
=======
    return render(request, 'index.html', {'orders': orders})


def inventory(request):
    items = Medicine.objects.all()
    return render(request,'inv.html',{'items': items})


>>>>>>> 67d417ebeb68daf6033828affe4db63efb8e6c65
