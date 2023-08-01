from django.urls import path,include
from rest_framework import routers
from .views import LecturerView, StudentView, ModuleView

router = routers.DefaultRouter()
router.register(r'lecturer', LecturerView, basename='lecturer')
router.register(r'student', StudentView, basename= 'student')
router.register(r'module', ModuleView, basename = 'module')

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework'))
]
