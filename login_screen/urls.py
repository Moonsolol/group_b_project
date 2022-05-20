from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = {
    path('', auth_views.LoginView.as_view(template_name='login_screen\login.html'),name='user_login'),
}