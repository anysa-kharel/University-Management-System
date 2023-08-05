from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'lecturer', views.LecturerView, basename='lecturer')
# router.register(r'student',views.StudentView,basename='student')
router.register(r'module', views.ModuleView, basename = 'module')
router.register(r'lecture', views.LectureView, basename='lecture')
router.register(r'tutor', views.TutorView, basename = 'tutor')
router.register(r'registration', views.RegistrationView, basename='registration')
# router.register(r'department', DepartmentView, basename='department')
router.register(r'semester', views.SemesterView, basename='semester')


urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_famework')),
    path('lecturer/update/<int:pk>/',views.LecturerView.as_view({'get': 'get', 'put': 'update', 'delete': 'delete'}), name='lecturer-detail'),
    # path('student/update/<int:pk>', views.StudentView.as_view({'get': 'get', 'put': 'update', 'delete': 'delete'}), name='student-detail'),
    path('student/<int:pk>',views.student_detail, name='student_detail'),
    path('student/', views.student_list, name = 'student_list'),
]
    # url(r'^$', student_list),
    # url(r'^(?P<pk>[0-9]+)', student_detail),