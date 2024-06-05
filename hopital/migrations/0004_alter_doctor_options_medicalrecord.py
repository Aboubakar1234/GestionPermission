# Generated by Django 4.2.2 on 2023-07-03 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopital', '0003_create_doctor_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'permissions': [('view_medical_record', 'Can view medical record'), ('edit_medical_record', 'Can edit medical record'), ('view_test_results', 'Can view test results'), ('view_medical_images', 'Can view medical images'), ('prescribe_medications', 'Can prescribe medications'), ('share_information', 'Can share information')]},
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hopital.patient')),
            ],
        ),
    ]