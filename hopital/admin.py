from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Doctor, Patient, Prescription, Nurse, AdministrativeStaff, Technician, Pharmacist, MedicalRecord


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'user_type']

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'specialization']
    
class PatientAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number']

class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'title']

class NurseAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number']

class AdministrativeStaffAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number']

class TechnicianAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number']

class PharmacistAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'first_name', 'last_name', 'email', 'phone_number']

class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ['patient', 'disease']


admin.site.register(Nurse, NurseAdmin)
admin.site.register(AdministrativeStaff, AdministrativeStaffAdmin)
admin.site.register(Technician, TechnicianAdmin)
admin.site.register(Pharmacist, PharmacistAdmin)

admin.site.register(MedicalRecord, MedicalRecordAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Prescription, PrescriptionAdmin)
