from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('reception/', views.reception_dashboard, name='reception_dashboard'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('employeelist/', views.employee_list, name='employee_list'),
    path('tabyouin/', views.tabyouin_list, name='tabyouin_list'),
    path('tabyouin/register/', views.tabyouin_register, name='tabyouin_register'),
    path('tabyouin/success/', views.tabyouin_success, name='tabyouin_success'),
    path('kensaku/', views.employee_kensaku, name='employee_kensaku'),
    path('updateemployee/', views.update_employee, name='update_employee'),
    path('updateemployee/<int:empid>', views.update_employee, name='update_employee'),
    path('confirm/', views.confirmupdate, name='confirmupdate'),
    path('patient_register/', views.patient_register, name='patient_register'),
    path('patient_success/', views.patient_success, name='patient_success'),
    path('patient_kensaku/', views.patient_kensaku, name='patient_kensaku'),
    path('update_hoken/', views.update_hoken, name='update_hoken'),
    path('update_hoken/<int:patid>', views.update_hoken, name='update_hoken'),
    path('confirm_update_hoken', views.confirm_update_hoken, name='confirm_update_hoken'),
    path('doctor_kensaku/', views.doctor_kensaku, name='doctor_kensaku'),
    path('medicine_cart/<int:patid>', views.medicine_cart, name='medicine_cart'),
]
