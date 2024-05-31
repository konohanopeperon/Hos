# forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid', 'emplname', 'empfname', 'emppasswd', 'emprole']
        widgets = {
            'emppasswd': forms.PasswordInput(),
        }