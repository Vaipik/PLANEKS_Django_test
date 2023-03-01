from django.urls import path

from . import views


app_name = "fake_schemas_generation"

urlpatterns = [
    path("", views.UserSchemasList.as_view(), name="user_schemas_list"),
    path("edit/<slug:schema_url>", views.EditUserSchema.as_view(), name="edit_user_schema"),
    path("<slug:schema_url>", views.UserSchema.as_view(), name="user_schema"),
    path("create_schema/", views.CreateUserSchema.as_view(), name="create_user_schema"),
]
