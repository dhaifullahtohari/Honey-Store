from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # توجيه روابط التطبيقات
    path('', include('catalog.urls')),       # الصفحة الرئيسية والمنتجات
    path('accounts/', include('accounts.urls')),  # تسجيل الدخول والتسجيل
    path('cart/', include('cart.urls')),          # سلة المشتريات
    path('orders/', include('orders.urls')),      # الطلبات
]

# دعم عرض ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
