from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from .. import services, models


class CreateDataSet(LoginRequiredMixin, View):
    def post(self, request, schema_url: str):
        try:
            rows_quantity = int(request.POST.get("rows quantity"))
        except ValueError:
            raise 404

        schema = services.get_user_schema(request.user, schema_url)
        services.create_dataset(schema, rows_quantity)
        messages.success(request, "Dataset has been created successfully")
        return redirect("fake_schemas_generation:user_schema", schema_url=schema_url)


class GenerateCSV(LoginRequiredMixin, View):
    """Generating CSV file by given dataset ID"""

    def post(self, request, dataset_id):
        dataset = services.get_dataset(dataset_id)
        services.generate_csv(dataset)

        return JsonResponse(data={"message": "Success", "status": 201}, status=200)


@login_required
def delete_dataset_file(request, dataset_id):
    """"""
    dataset = services.get_dataset(dataset_id)
    dataset.delete()
    messages.success(request, "Generated file was deleted")
    return JsonResponse(data={"message": "Success", "status": 204}, status=200)
