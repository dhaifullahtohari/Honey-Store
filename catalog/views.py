from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.filter(available=True)[:9]  # فقط 6 منتجات للعرض السريع
    return render(request, 'home.html', {'products': products})
