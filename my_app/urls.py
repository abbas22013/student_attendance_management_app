# my_app/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [ 
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', views.home, name='home'),
    path('classes/', views.class_list, name='class_list'),
    path('class/create/', views.class_create, name='class_create'),
    path('class/<int:class_id>/update/', views.class_update, name='class_update'),
    path('class/<int:class_id>/delete/', views.class_delete, name='class_delete'),
    path('students/', views.student_list, name='student_list'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/<int:student_id>/update/', views.student_update, name='student_update'),
    path('student/<int:student_id>/delete/', views.student_delete, name='student_delete'),  
]