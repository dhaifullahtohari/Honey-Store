from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'قيد الانتظار'),
        ('processing', 'قيد المعالجة'),
        ('shipped', 'تم الشحن'),
        ('completed', 'مكتمل'),
    ]

    user = models.ForeignKey(User, verbose_name="العميل", on_delete=models.CASCADE)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    status = models.CharField("الحالة", max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="الطلب", on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("الكمية")
    price = models.DecimalField("السعر (ريال)", max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "عنصر في الطلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.product.name} × {self.quantity}"
