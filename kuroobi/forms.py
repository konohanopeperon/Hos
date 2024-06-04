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

    def clean_tabyouinid(self):
        tabyouinid = self.cleaned_data.get('tabyouinid')
        if Tabyouin.objects.filter(tabyouinid=tabyouinid).exists():
            raise forms.ValidationError('この他病院IDはすでに存在します。')
        return tabyouinid

    def clean_tabyouintel(self):
        tabyouintel = self.cleaned_data.get('tabyouintel')
        if Tabyouin.objects.filter(tabyouintel=tabyouintel).exists():
            raise forms.ValidationError('この電話番号はすでに存在します。')
        return tabyouintel
