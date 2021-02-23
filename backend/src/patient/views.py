from django.views import View
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import os

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

class Assets(View):

    def get(self, _request, filename):
        path = os.path.join(os.path.dirname(__file__), 'static', filename)

        if os.path.isfile(path):
            with open(path, 'rb') as file:
                return HttpResponse(file.read(), content_type='application/javascript')
        else:
            return HttpResponseNotFound()