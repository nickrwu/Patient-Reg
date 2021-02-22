from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Patient
from .serializers import *

# Create your views here.

class PatientView(APIView):
	parser_classes = (MultiPartParser, FormParser)

	def get(self, request, *args, **kwargs):
		patients = Patient.objects.all().order_by('-id')
		serializer = PatientSerializer(patients, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		patients_serializer = PatientSerializer(data=request.data)
		if patients_serializer.is_valid():
			patients_serializer.save()
			return Response(patients_serializer.data, status=status.HTTP_201_CREATED)
		else:
			print('error', patients_serializer.errors)
			return Response(patients_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# @parser_classes([MultiPartParser, FormParser])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/patient-list/',
# 		'Info View':'/patient-info/<str:pk>/',
# 		'Create':'/patient-create/',
# 		'Update':'/patient-update/<str:pk>/',
# 		'Delete':'/patient-delete/<str:pk>/',
# 		}

# 	return Response(api_urls)

# @api_view(['GET'])
# def patientList(request):
# 	patients = Patient.objects.all().order_by('-id')
# 	serializer = PatientSerializer(patients, many=True)
# 	return Response(serializer.data)

# @api_view(['GET'])
# def patientInfo(request, pk):
# 	patients = Patient.objects.get(id=pk)
# 	serializer = PatientSerializer(patients, many=False)
# 	return Response(serializer.data)


# @api_view(['POST'])
# @parser_classes([MultiPartParser, FormParser])
# def patientCreate(request):
# 	serializer = PatientSerializer(data=request.data)

# 	if serializer.is_valid():
# 	    serializer.save()
# 	    return Response(status=status.HTTP_201_CREATED)
	
# 	return Response({
#     'data': serializer.data,
#     'message': 'Account could not be created with received data.',
#     'errors' : serializer.errors # for example
# }, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def patientUpdate(request, pk):
# 	patient = Patient.objects.get(id=pk)
# 	serializer = PatientSerializer(instance=task, data=request.data)

# 	if serializer.is_valid():
# 		serializer.save()

# 	return Response(serializer.data)


# @api_view(['DELETE'])
# def patientDelete(request, pk):
# 	patient = Patient.objects.get(id=pk)
# 	patient.delete()

# 	return Response('Info successfully delete!')