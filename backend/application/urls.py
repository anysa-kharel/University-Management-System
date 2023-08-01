from django.urls import path,include
from rest_framework import routers
from .views import LecturerView, StudentView

router = routers.DefaultRouter()
router.register(r'lecturer', LecturerView, basename='lecturer')
router.register(r'student', StudentView, basename= 'student')

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework'))
]
