import django_filters
from .models import School, Classroom, Teacher, Student

class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']

class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.CharFilter(field_name='school__name', lookup_expr='icontains')

    class Meta:
        model = Classroom
        fields = ['school']

class TeacherFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender']

class StudentFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter(lookup_expr='iexact')
    classroom = django_filters.CharFilter(field_name='classroom__grade', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom']
