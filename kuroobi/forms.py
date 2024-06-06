# forms.py
from django import forms
from .models import Employee, Tabyouin


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'emplname', 'empfname', 'emppasswd', 'emprole']
        widgets = {
            'emppasswd': forms.PasswordInput(),
        }


class TabyouinForm(forms.ModelForm):
    class Meta:
        model = Tabyouin
        fields = ['tabyouinid', 'tabyouinmei', 'abyouinaddres', 'tabyouintel', 'abyouinshihonkin', 'kyukyu']

