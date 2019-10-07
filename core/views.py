from django.shortcuts import render
from .models import Purchase
from .models import Medicine
# Create your views here.

def index(request):
    orders = Purchase.objects.all()
    return render(request, 'index.html', {'orders': orders})


def inventory(request):
    items = Medicine.objects.all()
    return render(request,'inv.html',{'items': items})


