from django.shortcuts import render
from .models import Purchase
# Create your views here.

def index(request):
    orders = Purchase.objects.all()
    return render(request, 'index.html', {'orders': orders})