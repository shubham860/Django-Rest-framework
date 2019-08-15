from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employee
from .serializer import employeeSerializer


class employeeList(APIView):
	def get(self,request):
		employee1 = employee.objects.all()
		Serializer = employeeSerializer(employee,many=True)
		return Response(Serializer.data)

	def post(self,request):
		pass	

