from django import forms
from django.core.exceptions import ValidationError

from ..libs import constants
from ..models import Schema, Column
from .column import ColumnForm


class SchemaForm(forms.ModelForm):

    class Meta:
        model = Schema
        fields = ["title", "separator", "quotes"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control mt-3",
                "placeholder": "Schema title"
            }),
            "separator": forms.Select(attrs={
                "class": "form-select mt-3",
                "placeholder": "Column separator"
            }),
            "quotes": forms.Select(attrs={
                "class": "form-select mt-3",
                "placeholder": "String quotes"
            }),
        }
        labels = {
            "title": "Schema title",
            "separator": "Column separator",
            "quotes": "String quotes",
        }

    def clean_title(self):
        """Used for validating minimum length of title which is set in constants"""
        title = self.cleaned_data["title"]
        if len(title) < constants.SCHEMA_TITLE_MIN_LENGTH:
            raise ValidationError(f"Title length can not be less than {constants.SCHEMA_TITLE_MIN_LENGTH} symbols")
        return title


ColumnFormSet = forms.inlineformset_factory(Schema, Column, ColumnForm, extra=1)
