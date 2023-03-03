from django.urls import path

from . import views


app_name = "fake_schemas_generation"

urlpatterns = [
    path(
        "edit_schema/<slug:schema_url>",
        views.EditUserSchema.as_view(),
        name="edit_user_schema",
    ),
    path(
        "delete_schema/<slug:schema_url>",
        views.delete_user_schema,
        name="delete_user_schema",
    ),
    path(
        "generate/<uuid:dataset_id>", views.GenerateCSV.as_view(), name="generate_csv"
    ),
    path(
        "new_dataset/<slug:schema_url>",
        views.CreateDataSet.as_view(),
        name="add_dataset",
    ),
    path(
        "delete_dataset/<uuid:dataset_id>",
        views.delete_dataset_file,
        name="delete_dataset",
    ),
    path("<slug:schema_url>", views.UserSchema.as_view(), name="user_schema"),
    path("create_schema/", views.CreateUserSchema.as_view(), name="create_user_schema"),
    path("", views.UserSchemasList.as_view(), name="user_schemas_list"),
]
