from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.user_auth.urls", namespace="user_auth")),
    path("", include("apps.fake_schemas_generation.urls", namespace="fake_schemas_generation"))
]
