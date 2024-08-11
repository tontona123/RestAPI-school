from rest_framework import viewsets
from apis.models import Teacher
from apis.serializers import TeacherSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['first_name', 'last_name', 'gender', 'classrooms__school']
