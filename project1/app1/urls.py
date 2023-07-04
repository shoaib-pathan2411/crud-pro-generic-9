from django.urls import path
from .views import StudentView, ShowView, UpdateView, DeleteView,SignupView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('sv/', StudentView.as_view(), name='student_url'),
    path('ssv/',ShowView.as_view(), name='show_url'),
    path('uv/<int:pk>/', UpdateView.as_view(), name='update_url'),
    path('del/<int:pk>/', DeleteView.as_view(), name='delete_url'),
    path('spv/',SignupView.as_view(), name='signup_url'),
    path('log/', LoginView.as_view(template_name = 'app1/login.html'), name='loginpage_url'),
    path('lot/', LogoutView.as_view(), name='logout_url')

]