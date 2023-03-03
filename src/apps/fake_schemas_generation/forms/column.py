from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from ..libs import constants
from ..models import Column


class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ["header", "type", "order", "start_integer", "end_integer", "sentences"]
        widgets = {
            "header": forms.TextInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "Column header",
                "required": True,
            }),
            "type": forms.Select(attrs={
                "class": "form-select mt-3",
                "placeholder": "Choose column type",
                "required": True,
            }),
            "order": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "Order №",
                "required": True,
            }),
            "start_integer": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "From",
            }),
            "end_integer": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "To",
            }),
            "sentences": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "Sentences quantity",
            }),
        }
        labels = {
            "header": "Column header",
            "type": "Column data type",
            "order": "Order №",
            "start_integer": "From",
            "end_integer": "To",
            "sentences": "Sentences quantity",
        }

    def clean_header(self):
        """Validating row header length. Miminal length is set in constants"""
        header = self.cleaned_data["header"]
        header_min_length = constants.COLUMN_HEADER_MIN_LENGTH
        if len(header) < header_min_length:
            raise ValidationError(f"Column header can not be less than {header_min_length} symbols")
        return header

    def clean_type(self):
        """To prevent make sure that user has changed the default data type"""
        column_type = self.cleaned_data["type"]
        if column_type == "df":
            raise ValidationError("Please choose data type")
        return column_type


class BaseColumnFormSet(BaseInlineFormSet):
    """FormSet to update the order of Settings in a Machine"""

    def clean(self):
        """Checks if there are no two Settings with the same order."""
        if any(self.errors):
            return
        orders = []
        sorted_form = sorted(self.forms, key=lambda f: f.cleaned_data["order"])
        for idx, form in enumerate(sorted_form, 1):

            if form.cleaned_data:
                order = form.cleaned_data["order"]
                column_type = form.cleaned_data["type"]
                if column_type == "i":  # Integer field
                    """Validating required fields for this field type"""
                    start_integer = form.cleaned_data.get("start_integer")
                    end_integer = form.cleaned_data.get("end_integer")
                    if start_integer is None:
                        form.add_error("start_integer", "Enter a number")
                    if end_integer is None:
                        form.add_error("end_integer", "Enter a number")
                    if start_integer and end_integer:
                        if start_integer < end_integer:
                            form.add_error("start_integer", "Can't be less than To")

                if column_type == "t":  # Text field
                    """Checking sentences field"""
                    sentences = form.cleaned_data.get("sentences")
                    if sentences is None:
                        form.add_error("sentences", "Enter a number")
                if idx != order:
                    form.add_error("order", "Ordering must be continuous numbering")

                if order in orders:
                    form.add_error("order", "The order of each column must be unique")
                else:
                    orders.append(order)
