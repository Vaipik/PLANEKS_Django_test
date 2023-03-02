from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View

from .. import services


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

    def post(self, request, dataset_id):

        dataset = services.get_dataset(dataset_id)
        # services.generate_csv(dataset)

        return JsonResponse(
            data={
                "message": "Success",
                "status": 201
            },
            status=200
        )
