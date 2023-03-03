from typing import Optional

from ..models import Schema
from ..forms import ColumnFormSet


def get_updated_formset(
    *,
    form_data: dict,
    formset: ColumnFormSet,
    button_data: str,
    instance: Optional[Schema] = None,
) -> ColumnFormSet:
    """
    This function is adding new form in column formset
    :param form_data: copied data from POST request
    :param formset: formset . DO NOT CALL
    :param button_data: Determines what action must be applied
    :param instance: parent instance for formset if exists.
    :return: updated formset
    """
    if button_data == "add":
        return _add_new_column(form_data, formset, instance)

    if button_data.isdigit():
        if button_data == "0":
            return formset(form_data)  # if inital formset
        return _delete_column(form_data, formset, button_data, instance)


def _add_new_column(
    form_data: dict, formset: ColumnFormSet, instance: Optional[Schema]
) -> ColumnFormSet:
    """Adding new form in column formset"""
    column_formset = (
        formset(form_data, instance=instance) if instance else formset(form_data)
    )
    if column_formset.is_valid():
        form_data["column-TOTAL_FORMS"] = int(form_data["column-TOTAL_FORMS"]) + 1
        column_formset = (
            formset(form_data, instance=instance) if instance else formset(form_data)
        )
    return column_formset


def _delete_column(
    form_data: dict,
    formset: ColumnFormSet,
    button_data: str,
    instance: Optional[Schema],
) -> ColumnFormSet:
    """
    Deleting column form with given id
    :param button_data: Stores id of column which must be deleted
    """
    pattern = f"column-{button_data}"
    for key in form_data.copy():
        if pattern in key:
            form_data.pop(key)
    form_data["column-TOTAL_FORMS"] = int(form_data["column-TOTAL_FORMS"]) - 1
    column_formset = (
        formset(form_data, instance=instance) if instance else formset(form_data)
    )
    return column_formset
