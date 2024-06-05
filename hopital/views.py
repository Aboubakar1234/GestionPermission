from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from .forms import PrescriptionForm
from django.core.exceptions import PermissionDenied
from .models import Doctor, Patient, UserProfile, MedicalRecord
from django.http import HttpResponse


def home(request):
    return render(request, 'base.html')

def registration(request):
    return render(request, 'registration.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.userprofile.user_type == 'DOCTOR':
                return redirect('doctor_homepage')
            else:
                return redirect('patient_homepage')
        else:
            # Invalid login
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    # GET request
    return render(request, 'login.html')

@login_required
def doctor_homepage(request):
    user_profile = UserProfile.objects.get(user=request.user)
    doctor = Doctor.objects.get(user_profile=user_profile)
    patients = Patient.objects.filter(doctor=doctor)
    prescriptions = doctor.prescription_set.all()

    return render(request, 'doctor_homepage.html', {'doctor': doctor, 'prescriptions': prescriptions, 'patients': patients})


@login_required
def patient_homepage(request):
    user_profile = UserProfile.objects.get(user=request.user)
    patient = Patient.objects.get(user_profile=user_profile)
    prescriptions = patient.prescription_set.all()

    return render(request, 'patient_homepage.html', {'patient': patient, 'prescriptions': prescriptions})

@login_required
@permission_required('hopital.view_medical_record', raise_exception=True)
def view_medical_record(request, record_id):
    # Récupérez l'enregistrement médical à partir de l'ID
    record = get_object_or_404(MedicalRecord, id=record_id)

    # Assurez-vous que le doctor connecté a la permission de voir cet enregistrement médical
    if not request.user.has_perm('hopital.view_medical_record'):
        return HttpResponse('Vous n\'avez pas la permission de voir cet enregistrement médical.', status=403)

    # Renvoyez les détails de l'enregistrement médical
    return render(request, 'view_medical_record.html', {'record': record})

@login_required
@permission_required('hopital.add_prescription', raise_exception=True)
def add_prescription(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    doctor = Doctor.objects.get(user_profile=request.user.userprofile)

    # Vérifier que le patient appartient au médecin connecté
    if doctor != patient.doctor:
        raise PermissionDenied

    # Vérifier que le médecin a la permission d'ajouter une prescription
    if not request.user.has_perm('hopital.add_prescription'):
        raise PermissionDenied

    # Créer une nouvelle prescription
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            prescription = form.save(commit=False)
            prescription.doctor = doctor
            prescription.patient = patient
            prescription.save()
            return redirect('doctor_homepage')  # rediriger vers une autre vue après la création de la prescription
    else:
        form = PrescriptionForm()

    return render(request, 'add_prescription.html', {'form': form})

    # @login_required
#@permission_required('hopital.edit_medical_record', raise_exception=True)
#def edit_medical_record(request, record_id):
    # Retrieve the medical record based on the ID
 #   record = get_object_or_404(MedicalRecord, id=record_id)

    # Check if the logged-in user has the permission to edit the medical record
  #  if not request.user.has_perm('hopital.edit_medical_record'):
   #     return HttpResponse('You do not have permission to edit this medical record.', status=403)

    # Handle the form submission for editing the medical record
    ##if request.method == 'POST':
      #  form = MedicalRecordForm(request.POST, instance=record)
       # if form.is_valid():
        #    form.save()
         #   return redirect('view_medical_record', record_id=record_id)
    #else:
     #   form = MedicalRecordForm(instance=record)

    #return render(request, 'edit_medical_record.html', {'form': form, 'record': record})
