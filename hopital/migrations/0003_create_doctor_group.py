# Generated by Django 4.2.2 on 2023-07-03 09:21

from django.db import migrations
from django.contrib.auth.models import User


def create_doctor_group(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Doctor = apps.get_model('hopital', 'Doctor')

    # Get or create the doctor group
    doctor_group, created = Group.objects.get_or_create(name='Doctor')

    # Get the Doctor model
    doctor_content_type = ContentType.objects.get_for_model(Doctor)

    # Create the permissions
    permissions_codenames = [
        'view_medical_record',
        'edit_medical_record',
        'view_test_results',
        'view_medical_images',
        'add_prescription',
        'share_information',
    ]

    permissions = []
    for codename in permissions_codenames:
        permission, created = Permission.objects.get_or_create(
            codename=codename,
            content_type=doctor_content_type,
        )
        permissions.append(permission)

    # Set the permissions to the doctor group
    doctor_group.permissions.set(permissions)

    User = apps.get_model('auth', 'User')

    # Try to get the 'borel' user and add him to the doctor group
    try:
        user = User.objects.get(username='borel')
        doctor_group.user_set.add(user)
    except User.DoesNotExist:
        # Handle the case where the 'borel' user does not exist
        pass

class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0002_patient_doctor_alter_userprofile_user_type_and_more'),
    ]

    operations = [
        migrations.RunPython(create_doctor_group),
    ]