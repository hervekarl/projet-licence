from django.shortcuts import render
from rest_framework import generics
from .save_patient_serializer import *
from .models import *

class DeletePatient(generics.DestroyAPIView):
    queryset=Patient.objects.using('patient').all()
    serializer_class=PatientSerialiser
    
class ListePatient(generics.ListAPIView):
    queryset=Patient.objects.using("patient").all()
    serializer_class=PatientSerialiser

class ListCreatePatient(generics.ListCreateAPIView):
    queryset=Patient.objects.using("patient").all()
    serializer_class=PatientSerialiser

class UpdatePatient(generics.UpdateAPIView):
    queryset=Patient.objects.using('patient').all()
    serializer_class=PatientSerialiser
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class DetailPatient(generics.RetrieveAPIView):
    queryset=Patient.objects.using('patient').all()
    serializer_class=PatientSerialiser