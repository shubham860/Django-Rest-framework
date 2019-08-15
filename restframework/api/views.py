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
		employees = employee.objects.all()
		Serializer = employeeSerializer(employees,many=True)
		return Response(Serializer.data)

	def post(self,request):
		pass

# from rest_framework import generics
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from .models import employee
# from .serializer import employeeSerializer

# class employeeListAPIView(generics.ListAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]


# class employeeRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = employee.objects.all()
#     serializer_class = employeeSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     lookup_field = 'emp_id'	

