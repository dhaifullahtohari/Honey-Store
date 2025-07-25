# orders/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import CartItem
from .models import Order, OrderItem

# -----------------------------
# إنشاء الطلب من السلة
# -----------------------------
@login_required
def create_order(request):
    cart_items = CartItem.objects.filter(user=request.user)

    if not cart_items.exists():
        messages.warning(request, "سلة المشتريات فارغة.")
        return redirect('cart:cart_detail')  # تأكد أن لديك هذا العرض

    try:
        # إنشاء الطلب
        order = Order.objects.create(user=request.user)

        # إنشاء عناصر الطلب من عناصر السلة
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # حذف عناصر السلة بعد إنشاء الطلب
        cart_items.delete()

        messages.success(request, "تم إنشاء الطلب بنجاح.")
        return render(request, 'orders/order_confirmation.html', {'order': order})

    except Exception as e:
        messages.error(request, "حدث خطأ أثناء معالجة الطلب. الرجاء المحاولة مرة أخرى.")
        # من الأفضل تسجيل الخطأ في ملف لسهولة التتبع
        print(f"خطأ في إنشاء الطلب: {e}")
        return redirect('cart:cart_detail')
