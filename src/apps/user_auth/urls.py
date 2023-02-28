from django.urls import path

from . import views


app_name = "user_auth"

urlpatterns = [
    path("sign_in/", views.SignInView.as_view(), name="login"),
    path("sign_up/", views.SignUpView.as_view(), name="registration"),
    path("sign_out/", views.SignOutView.as_view(), name="logout"),
]
