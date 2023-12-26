from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_api.models import Employee
from rest_api.serializer import Emp_serializer


# Create your views here.

@api_view(['GET','POST'])
def emp_list(request):

    if request.method =='GET':
        employees = Employee.objects.all()
        serializer=Emp_serializer(employees,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = Emp_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE']

def emp_details(request,pk):
    try:
        employees = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Emp_serializer(employees)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Emp_serializer(employees,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employees.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

