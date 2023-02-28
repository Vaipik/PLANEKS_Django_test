from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View, generic

from . import forms


class SignUpView(generic.CreateView):
    """Registraion view"""
    template_name = 'user_auth/sign_up.html'
    form_class = forms.SignUpForm

    def get_success_url(self):
        login(self.request, self.object)  # self.object -> created user
        return reverse_lazy("fake_schemas_generation:user_schemas")


class SignInView(View):
    """Accepts AJAX request from sign in modal form and login user."""
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            user = authenticate(username=username, password=password)  # If user exists
            if user:
                login(request, user)
                return JsonResponse(
                    data={
                        "message": "Logged in",
                        "status": 200,
                        "url": redirect("user_profile:profile").url
                    },
                    status=200
                )

        return JsonResponse(
                data={"message": "Invalid credentials", "status": 400},
                status=200
        )


class SignOutView(LoginRequiredMixin, View):
    """Accepts POST request form sign out modal form and signing out user.
    Afterwards redirecting user to registartion page"""
    def post(self, request):
        logout(request)
        return redirect("user_auth:registration")
