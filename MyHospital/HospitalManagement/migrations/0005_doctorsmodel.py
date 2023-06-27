# Generated by Django 4.1.2 on 2023-06-06 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalManagement', '0004_aboutmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DoctorImage', models.ImageField(upload_to='images')),
                ('DoctorName', models.CharField(max_length=300)),
                ('DoctorExpertize', models.CharField(max_length=300)),
            ],
        ),
    ]
