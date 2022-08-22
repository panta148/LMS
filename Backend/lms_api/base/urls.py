from django.urls import path
from . import views
urlpatterns = [
    path('teacher/', views.TeacherList.as_view(), name='Teacher'),
    path('teacher/<int:pk>/', views.TeacherDetail.as_view(), name='TeacherDetail'),
    path('student/', views.StudentList.as_view(), name='Student'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='StudentDetail'),
    path('coursecategory/', views.CourseCategoryList.as_view(), name='category'),
    path('coursecategory/<int:pk>/',
         views.CourseCategoryDetail.as_view(), name='categoryDetail'),
    path('course/', views.CourseList.as_view(), name='course'),
    path('course/<int:pk>/',
         views.CourseDetail.as_view(), name='courseDetail'),

]
