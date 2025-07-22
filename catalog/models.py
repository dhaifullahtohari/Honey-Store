from django.db import models

class Product(models.Model):
    name = models.CharField("اسم المنتج", max_length=200)
    description = models.TextField("الوصف")
    price = models.DecimalField("السعر (ريال)", max_digits=8, decimal_places=2)
    image = models.ImageField("صورة المنتج", upload_to='products/')
    available = models.BooleanField("متوفر في المخزون؟", default=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
