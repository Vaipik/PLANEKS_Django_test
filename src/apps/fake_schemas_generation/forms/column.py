from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField

from ..libs import constants
from ..models import Record


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Record
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
                "required": True,
            }),
            "end_integer": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "To",
                "required": True,
            }),
            "sentences": forms.NumberInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "Sentences quantity",
                "required": True,
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
        """"""
        type = self.cleaned_data["type"]
        if type == "df":
            raise ValidationError("Please choose data type")
        return type
