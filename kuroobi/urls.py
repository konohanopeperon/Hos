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
    path('update_employee/', views.update_employee, name='update_employee'),
    path('tabyouin/register/', views.tabyouin_register, name='tabyouin_register'),
    path('tabyouin/confirm/', views.tabyouin_confirm, name='tabyouin_confirm'),
    path('tabyouin/success/', views.tabyouin_success, name='tabyouin_success'),
]