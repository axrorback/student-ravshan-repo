from django.apps import AppConfig
from django.shortcuts import render
from .models import Student
# Create your views here.


def index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})
def student_detail(request, slug):
    student = Student.objects.get(slug=slug)
    return render(request, 'student/student.html', {'student': student})


