from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import CustomUser

# -------------------------------
# إنشاء حساب مستخدم جديد (تسجيل)
# -------------------------------
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # التحقق من تطابق كلمتي المرور
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين.")
            return redirect('accounts:signup')

        # التحقق من تكرار اسم المستخدم
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect('accounts:signup')

        # التحقق من تكرار رقم الجوال
        if CustomUser.objects.filter(mobile=mobile).exists():
            messages.error(request, "رقم الجوال مستخدم بالفعل.")
            return redirect('accounts:signup')

        # التحقق من تكرار البريد الإلكتروني (تحذير فقط)
        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, "البريد الإلكتروني مستخدم من قبل.")

        # إنشاء المستخدم
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            mobile=mobile,
            password=password1
        )

        # تسجيل الدخول مباشرة بعد الإنشاء
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/signup.html')


# -------------------------------
# تسجيل الدخول
# -------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "اسم المستخدم أو كلمة المرور غير صحيحة.")
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request, "تم تسجيل الخروج بنجاح.")
    return redirect('accounts:login')
