from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'lecturer', LecturerView, basename='lecturer')
# router.register(r'student_list',student_list,basename='student-list')
# router.register(r'module', ModuleView, basename = 'module')
# router.register(r'lecture', LectureView, basename='lecture')
# router.register(r'tutor', TutorView, basename = 'tutor')
# router.register(r'registration', RegistrationView, basename='registration')
# # router.register(r'department', DepartmentView, basename='department')
# router.register(r'semester', SemesterView, basename='semester')


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework')),
    # path('lecturer/update/<int:pk>/',LecturerView.as_view({'get': 'get', 'put': 'update', 'delete': 'delete'}), name='lecturer-detail'),
    path('student/', views.student_list, name = 'student_list'),
    path('student/<int:pk>',views.student_detail, name='student_detail'),
]
    # url(r'^$', student_list),
    # url(r'^(?P<pk>[0-9]+)', student_detail),