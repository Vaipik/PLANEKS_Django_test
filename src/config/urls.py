from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.user_auth.urls", namespace="user_auth")),
    path(
        "",
        include(
            "apps.fake_schemas_generation.urls", namespace="fake_schemas_generation"
        ),
    ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = "apps.exceptions.views.handler_400"
handler403 = "apps.exceptions.views.handler_403"
handler404 = "apps.exceptions.views.handler_404"
handler500 = "apps.exceptions.views.handler_500"
