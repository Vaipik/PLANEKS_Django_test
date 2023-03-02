from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import generic, View

from utils.pagination import PaginationMixin
from .. import forms, services


class CreateUserSchema(LoginRequiredMixin, View):
    """View for creating new user schema with form and inline formset"""

    def get(self, request):
        context = {
            "form": forms.SchemaForm(),
            "column_formset": forms.ColumnFormSet()
        }
        return render(request, "fake_schemas_generation/create_schema.html", context)

    def post(self, request):
        """Processing POST request from form and formset.
        Update formset forms and saving form and formset instances to DB"""
        form_data: dict = request.POST.copy()
        form = forms.SchemaForm(form_data)
        button = form_data.get("button")
        if button == "submit":  # Submit form
            if form.is_valid():
                schema = form.save(commit=False)
                schema.user = request.user
                formset = forms.ColumnFormSet(form_data, instance=schema)
                print(formset.errors)
                if formset.is_valid():
                    schema.save()
                    formset.save()
                    return redirect("fake_schemas_generation:user_schemas_list")

                return render(request, "fake_schemas_generation/create_schema.html",
                              {"form": form, "column_formset": formset})
        formset = services.get_updated_formset(
            form_data=form_data,
            formset=forms.ColumnFormSet,
            button_data=button
        )
        return render(request, "fake_schemas_generation/create_schema.html", {"form": form, "column_formset": formset})


class EditUserSchema(LoginRequiredMixin, View):
    """View for editing new user schema with form and inline formset"""

    def get(self, request, schema_url: str):
        schema = services.get_user_schema(request.user, schema_url)
        form = forms.SchemaForm(instance=schema)
        formset = forms.ColumnFormSet(instance=schema)
        context = {
            "schema_url": schema_url,
            "form": form,
            "column_formset": formset
        }
        return render(request, "fake_schemas_generation/edit_schema.html", context)

    def post(self, request, schema_url):
        """Processing POST request from form and formset.
        Update formset forms and saving form and formset instances to DB"""
        schema = services.get_user_schema(request.user, schema_url)
        form_data: dict = request.POST.copy()
        form = forms.SchemaForm(form_data, instance=schema)
        button = form_data.get("button")
        if button == "submit":  # Submit form
            if form.is_valid():
                schema = form.save(commit=False)
                schema.user = request.user
                print(schema)
                formset = forms.ColumnFormSet(form_data, instance=schema)
                print(formset.errors)
                if formset.is_valid():
                    schema.save()
                    formset.save()
                    return redirect("fake_schemas_generation:user_schemas_list")

                return render(
                    request,
                    "fake_schemas_generation/edit_schema.html",
                    {
                        "schema_url": schema_url,
                        "form": form,
                        "column_formset": formset
                    }
                )
        formset = services.get_updated_formset(
            form_data=form_data,
            formset=forms.ColumnFormSet,
            button_data=button,
            instance=schema,
        )

        return render(
            request,
            "fake_schemas_generation/edit_schema.html",
            {
                "schema_url": schema_url,
                "form": form,
                "column_formset": formset
            }
        )


class UserSchemasList(LoginRequiredMixin, PaginationMixin, generic.ListView):
    template_name = 'fake_schemas_generation/schemas_list.html'
    context_object_name = "schemas"
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(
            **kwargs,
            title="Schemas list",
        )
        context.update(**self.get_pages(page_obj=context["page_obj"]))
        return context

    def get_queryset(self):
        return services.get_user_schemas(self.request.user)


class UserSchema(LoginRequiredMixin, PaginationMixin, generic.ListView):
    """Displaying schema columns and schemas datasets"""
    template_name = "fake_schemas_generation/schema_detail.html"
    slug_url_kwarg = "schema_url"
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(
            **kwargs,
            schema=self.schema,
            title=self.schema.title,
        )
        context.update(**self.get_pages(page_obj=context["page_obj"]))
        return context

    def get_queryset(self):
        self.schema = services.get_user_schema(self.request.user, schema_url=self.kwargs["schema_url"])
        return services.get_schema_datasets(self.schema)
