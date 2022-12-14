from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("signup/",views.signup,name="signup"),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='signup/login.html'),name='login'),
    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='signup/change_password.html'),name='change_pass'),
    path('change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='signup/done.html'),name='password_change_done'),
    path('account/',views.UserUpdateView.as_view(),name='my_account'),
]