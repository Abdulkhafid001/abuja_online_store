from django.http import HttpResponse
from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Students
from .serializers import studentSerializer


class Get_students_List(APIView):
    def get(self, request):
        students = Students.objects.all()
        serializer_class = studentSerializer(students, many=True)
        return Response(serializer_class.data)


def homepage(request):
    return render(request, 'index.html')
