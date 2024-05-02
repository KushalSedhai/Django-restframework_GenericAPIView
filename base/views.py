from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class Studentview(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self,request):
        data = self.get_queryset()
        serializer = self.serializer_class(data, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("DATA IS CREATED")
        else:
            return Response(serializer.errors)

class StudentDetailView(GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get(self, request,  pk):
        try:
            data = Student.objects.get(id=pk)
        except:
            return Response("Data not found", status = status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(data)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            datum = Student.objects.get(id=pk)
        except:
            return Response("Data not found", status = status.HTTP_404_NOT_FOUND)    
        serializer = self.serializer_class(datum, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("DATA IS UPDATED")
        else:
              return Response(serializer.errors)

    def delete(self, request, pk ):
        try:
            data = Student.objects.get(id=pk)
        except:
            return Response("Data is nofound",  status=status.HTTP_404_NOT_FOUND)
        data.delete()
        return Response("Data is deleted")