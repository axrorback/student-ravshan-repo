from django.urls import path
from .views import index, student_detail

urlpatterns = [
    path('', index, name='index'),
    path('student/<slug:slug>/', student_detail, name='student'),
]

