from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = (
        ('DOCTOR', 'Doctor'),
        ('PATIENT', 'Patient'),
        ('NURSE', 'Nurse'),
        ('ADMINISTRATIVE', 'Administrative'),
        ('TECHNICIAN', 'Technician'),
        ('PHARMACIST', 'Pharmacist'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=USER_TYPES)

class Doctor(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True, limit_choices_to={'user_type': 'DOCTOR'})
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    specialization = models.CharField(max_length=50, null=True)

    class Meta:
        permissions = [
            ("view_medical_record", "Can view medical record"),
            ("edit_medical_record", "Can edit medical record"),
            ("view_test_results", "Can view test results"),
            ("view_medical_images", "Can view medical images"),
            ("add_prescription", "Can add prescription"),
            ("share_information", "Can share information"),
        ]


class Patient(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'PATIENT'})
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)

class MedicalRecord(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    disease = models.CharField(max_length=100)

class Prescription(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)

class Nurse(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'NURSE'})
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    ward = models.CharField(max_length=50, null=True)  # Specific field

class AdministrativeStaff(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'ADMINISTRATIVE'})
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    job_title = models.CharField(max_length=50, null=True)  # Specific field

class Technician(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'TECHNICIAN'})
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    specialty = models.CharField(max_length=50, null=True)  # Specific field

class Pharmacist(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, limit_choices_to={'user_type': 'PHARMACIST'})
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email = models.EmailField(max_length=254, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    pharmacy_name = models.CharField(max_length=100, null=True)  # Specific field
