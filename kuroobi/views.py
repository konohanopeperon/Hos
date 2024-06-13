from django.utils import timezone

from django.shortcuts import render, redirect

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from .forms import EmployeeForm, TabyouinForm
from .models import Employee, Tabyouin, Patient
from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render, get_object_or_404, redirect


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
                return render(request, 'Kadai1/L100/reception.html', {'empid': empid})
            elif employee.emprole == 2:
                return render(request, 'Kadai1/L100/doctor.html', {'empid': empid})
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
            return render(request, 'Kadai1/L100/Admin.html')

    return render(request, 'Kadai1/E100/Registeremployee.html')


def employee_list(request):
    if request.method == 'GET':
        employees = Employee.objects.all()
        return render(request, 'Kadai1/E100/UpdateEmployee.html', {'employees': employees})


def employee_kensaku(request):
    query = request.GET.get('query')
    if query:
        employees = Employee.objects.filter(empid__icontains=query)
    else:
        employees = Employee.objects.all()
    return render(request, 'Kadai1/E100/UpdateEmployee.html', {'employees': employees, 'query': query})


def update_employee(request, empid):
    employee = get_object_or_404(Employee, empid=empid)
    if request.method == 'POST':
        new_password = request.POST['new_password']
        confirm_new_password = request.POST['confirm_new_password']

        if new_password != confirm_new_password:
            messages.error(request, 'パスワードが一致しません')
        return render(request, 'Kadai1/E100/confirmpassword.html', {'employee': employee, 'new_password': new_password})
    return render(request, 'Kadai1/E100/passwordupdate.html', {'employee': employee})


def confirmupdate(request):
    if request.method == 'POST':
        empid = request.POST.get('empid')
        new_password = request.POST.get("new_password")
        employee = Employee.objects.get(empid=empid)
        employee.emppasswd = new_password
        employee.save()
    return render(request, 'Kadai1/E100/successupdate.html')


def tabyouin_list(request):
    query = request.GET.get('q')
    if query:
        tabyouins = Tabyouin.objects.filter(abyouinaddres__icontains=query)
    else:
        tabyouins = Tabyouin.objects.all()
    return render(request, 'Kadai1/H100/tabyouin_list.html', {'tabyouins': tabyouins, 'query': query})


def tabyouin_register(request):
    if request.method == 'POST':
        tabyouinid = request.POST.get('tabyouinid')
        tabyouinmei = request.POST.get('tabyouinmei')
        abyouinaddres = request.POST.get('abyouinaddres')
        tabyouintel = request.POST.get('tabyouintel')
        abyouinshihonkin = request.POST.get('abyouinshihonkin')
        kyukyu = request.POST.get('kyukyu')

        if Tabyouin.objects.filter(tabyouinid=tabyouinid, tabyouinmei=tabyouinmei, abyouinaddres=abyouinaddres,
                                   tabyouintel=tabyouintel, abyouinshihonkin=abyouinshihonkin, kyukyu=kyukyu).exists():
            messages.error(request, 'この病院はすでに登録されています。')
        else:
            tabyouin = Tabyouin(tabyouinid=tabyouinid, tabyouinmei=tabyouinmei, abyouinaddres=abyouinaddres,
                                tabyouintel=tabyouintel, abyouinshihonkin=abyouinshihonkin, kyukyu=kyukyu)
            tabyouin.save()
            return redirect('tabyouin_success')
    return render(request, 'Kadai1/H100/tabyouin_register.html')


def tabyouin_success(request):
    return render(request, 'Kadai1/H100/tabyouin_success.html')


def patient_register(request):
    if request.method == 'POST':
        patid = request.POST.get('patid')
        patfname = request.POST.get('patfname')
        patlname = request.POST.get('patlname')
        hokenmei = request.POST.get('hokenmei')
        hokenexp = request.POST.get('hokenexp')

        if Patient.objects.filter(patid=patid, patfname=patfname, patlname=patlname, hokenmei=hokenmei,
                                  hokenexp=hokenexp).exists():
            messages.error(request, 'この患者はすでに登録されています。')
        else:
            patient = Patient(patid=patid, patfname=patfname, patlname=patlname, hokenmei=hokenmei, hokenexp=hokenexp)
            patient.save()
            return redirect('patient_success')
    return render(request, 'Kadai1/P100/patient_register.html')


def patient_success(request):
    return render(request, 'Kadai1/P100/patient_success.html')


def update_hoken(request, patid):
    patient = get_object_or_404(Patient, patid=patid)
    if request.method == 'POST':
        new_hokenmei = request.POST['new_hokenmei']
        new_hokenexp = request.POST['new_hokenexp']

        return render(request, 'Kadai1/P100/confirm_update_hoken.html',
                      {'patient': patient, 'new_hokenmei': new_hokenmei, 'new_hokenexp': new_hokenexp})
    return render(request, 'Kadai1/P100/update_hoken.html', {'patient': patient})


def confirm_update_hoken(request):
    if request.method == 'POST':
        patid = request.POST.get('patid')
        new_hokenmei = request.POST.get("new_hokenmei")
        new_hokenexp = request.POST.get("new_hokenexp")
        patient = Patient.objects.get(patid=patid)
        patient.hokenmei = new_hokenmei
        patient.hokenexp = new_hokenexp
        patient.save()
    return render(request, 'Kadai1/P100/success_update_hoken.html')


def patient_kensaku(request):
    query = request.GET.get('query')
    today = timezone.now().date()
    patients = []
    if query:
        patienter = Patient.objects.all()
        for patient in patienter:
            if patient.hokenexp <= today:
                patients.append(patient)

    else:
        patients = Patient.objects.all()
    return render(request, 'Kadai1/P100/patient_list.html', {'patients': patients, 'query': query})
