from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'module', views.ModuleView, basename = 'module')
router.register(r'lecture', views.LectureView, basename='lecture')
router.register(r'tutor', views.TutorView, basename = 'tutor')
router.register(r'registration', views.RegistrationView, basename='registration')
router.register(r'semester', views.SemesterView, basename='semester')


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework')),

    path('lecturer/',views.lecturer_list,name='lecturer_list'),
    path('lecturer/update/<int:pk>/',views.lecturer_detail, name = 'lecturer_detail'),
    path('student/', views.student_list, name = 'student_list'),
    path('student/update/<int:pk>/',views.student_detail, name='student_detail'),

    path('semester/', views.semester_list, name = 'semester_list'),
    path('semester/<str:pk>/',views.semester_detail, name='semester_detail'),
    path('semester/<str:faculty>/<int:pk>/',views.semester_details, name='semester_detail'),

    path('form/',views.form_list,name='form_list'),
    path('form/<int:pk>',views.form_details,name='form_details'),
]
