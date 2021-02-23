from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import os

from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status, viewsets

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.

class PatientView(viewsets.ModelViewSet):
	parser_classes = (MultiPartParser, FormParser)

	queryset = Patient.objects.all().order_by('-id')
	serializer_class = PatientSerializer

	@action(detail=True, methods=['POST'])
	def post(self, request):
		patients_serializer = PatientSerializer(data=request.data)
		if patients_serializer.is_valid():
			patients_serializer.save()
			return Response(patients_serializer.data, status=status.HTTP_201_CREATED)
		else:
			print('error', patients_serializer.errors)
			return Response(patients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	@action(detail=False)
	def get(self, request):
		patients = Patient.objects.all().order_by('-id')
		serializer = PatientSerializer(patientss, many=True)
		return Response(serializer.data)

class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()