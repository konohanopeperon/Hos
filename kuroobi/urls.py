from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='index'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('reception/', views.reception_dashboard, name='reception_dashboard'),
    path('doctor/', views.doctor_dashboard, name='doctor_dashboard'),
    path('login/', views.login, name='login'),
    path('menu/', views.menu_view, name='menu'),
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
]
