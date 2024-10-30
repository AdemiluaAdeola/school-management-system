from django.urls import path
from user.views import *

urlpatterns = [
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
]
