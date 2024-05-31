from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import EmployeeForm
from .models import Employee


def login_view(request):
    if request.method == 'POST':
        empid = request.POST['empid']
        password = request.POST["password"]
        try:
            employee = Employee.objects.get(empid=empid)
        except Employee.DoesNotExist:
            messages.error(request, "ユーザIDもしくはパスワードが違います")
            return render(request, 'Kadai1/L100/login.html')

        if employee.emppasswd == password:  # Here, normally you should hash and verify the password
            request.session['empid'] = employee.empid
            if employee.emprole == 0:
                return render(request, 'Kadai1/L100/admin.html')
            elif employee.emprole == 1:
                return render(request, 'Kadai1/L100/reception.html')
            elif employee.emprole == 2:
                return render(request, 'Kadai1/L100/doctor.html')
        else:
            messages.error(request, "ユーザIDもしくはパスワードが違います")
            return render(request, 'Kadai1/L100/login.html')
    return render(request, 'Kadai1/L100/login.html')


def menu_view(request):
    return render(request, 'Kadai1/L100/Menu.html')


def logout_view(request):
    logout(request)
    return redirect('Kadai1/L100/Login.html')


def admin_dashboard(request):
    return render(request, 'Kadai1/L100/Admin.html')


def reception_dashboard(request):
    return render(request, 'Kadai1/L100/Reception.html')


def doctor_dashboard(request):
    return render(request, 'Kadai1/L100/Doctor.html')


def admin_check(user):
    return user.is_superuser


def register_employee(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        empfname = request.POST.get('empfname')
        emplname = request.POST.get('emplname')
        emppasswd = request.POST.get('emppasswd')
        emprole = request.POST.get('emprole')

        if Employee.objects.filter(empid=empid).exists():
            messages.error(request, 'このユーザーIDは既に存在します。')
        else:
            employee = Employee(empid=empid, empfname=empfname, emplname=emplname, emppasswd=emppasswd, emprole=emprole)
            employee.save()
            messages.success(request, '従業員が正常に登録されました。')
            return redirect('Admin.html')

    return render(request, 'Kadai1/E100/registeremployee.html')


def update_employee(request):
    if request.method == 'POST':
        current_user = request.user
        new_password = request.POST.get('emppasswd')

        if Employee.objects.filter(empid=current_user.username).exists():
            employee = Employee.objects.get(empid=current_user.username)
            employee.emppasswd = new_password
            employee.save()
            messages.success(request, 'パスワードが正常に更新されました。')
        else:
            messages.error(request, '従業員情報が見つかりませんでした。')

            return redirect('update_employee')
    return render(request, 'Kadai1/E100/updateemployee.html')
