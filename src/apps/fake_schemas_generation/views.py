from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic, View

from . import forms, models, services


class CreateUserSchema(LoginRequiredMixin, View):

    def get(self, request):
        context = {
            "form": forms.CreatSchemaForm(),
            "column_formset": forms.ColumnFormSet()
        }
        return render(request, "fake_schemas_generation/create_schema.html", context)

    def post(self, request):
        form_data: dict = request.POST.copy()
        form = forms.CreatSchemaForm(form_data)
        button = form_data.get("button")
        if button == "submit":
            pass

        formset = services.get_updated_formset(
            form_data=form_data,
            formset=forms.ColumnFormSet,
            button_data=button
        )
        return render(request, "fake_schemas_generation/create_schema.html", {"form": form, "column_formset": formset})


class EditUserSchema(LoginRequiredMixin, generic.UpdateView):
    pass


class UserSchemasList(LoginRequiredMixin, generic.ListView):
    template_name = 'fake_schemas_generation/schemas_list.html'
    context_object_name = "schemas"
    extra_context = {"title": "Schemas list"}

    def get_queryset(self):
        return services.get_user_schemas(self.request.user)


class UserSchema(LoginRequiredMixin, generic.DetailView):
    pass
