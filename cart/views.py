# cart/views.py
from django.shortcuts import get_object_or_404, redirect
from catalog.models import Product
from .models import CartItem
from django.contrib import messages

def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        messages.warning(request, "يجب تسجيل الدخول لإضافة المنتجات إلى السلة.")
        return redirect('accounts:login')

    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user, product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    messages.success(request, f"تم إضافة {product.name} إلى السلة.")
    return redirect('catalog:home')
# cart/views.py

from django.shortcuts import render, redirect
from .models import CartItem

def cart_detail(request):
    if not request.user.is_authenticated:
        return redirect('accounts:login')

    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'cart/cart_detail.html', context)
