from django.db import models

# Create your models here.


class PatientCheckinVisitModel(models.Model):
    id = models.AutoField(primary_key = True)
    patient_id = models.IntegerField(null = False, blank = False)
    doctor_id = models.IntegerField(null = False, blank = False) #This should idealy be the doctor id in integer
    checkin_time = models.DateTimeField(null = False, blank = False)
    in_session_time = models.DateTimeField(null = True, blank = True)

