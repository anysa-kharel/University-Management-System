from django.urls import path,include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'lecturer', LecturerView, basename='lecturer')
router.register(r'student', StudentView, basename= 'student')
router.register(r'module', ModuleView, basename = 'module')
router.register(r'lecture', LectureView, basename='lecture')
router.register(r'tutor', TutorView, basename = 'tutor')
router.register(r'registration', RegistrationView, basename='registration')
# router.register(r'department', DepartmentView, basename='department')
router.register(r'semester', SemesterView, basename='semester')

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework'))
]
