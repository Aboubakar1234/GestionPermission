from django.urls import path
from hopital import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login'),
     path('doctor_homepage/', views.doctor_homepage, name='doctor_homepage'),
    path('patient_homepage/', views.patient_homepage, name='patient_homepage'),
    path('add_prescription/<int:patient_id>/', views.add_prescription, name='add_prescription'),
    path('medical_records/<int:record_id>/', views.view_medical_record, name='view_medical_record'),
    # path('edit_medical_record/<int:record_id>/', views.edit_medical_record, name='edit_medical_record'),
]
