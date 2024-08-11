# apis/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.v1 import SchoolViewSet, ClassroomViewSet, TeacherViewSet, StudentViewSet, summary_view

router = DefaultRouter()
router.register(r'schools', SchoolViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('summary/', summary_view, name='summary'), 
]
