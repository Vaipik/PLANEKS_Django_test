def get_updated_formset(*, form_data: dict, formset, button_data: str):
    """
    This function is adding new form in column formset
    :param form_data: copied data from POST request
    :param formset: formset . DO NOT CALL
    :param button_data: Determines what action must be applied
    :return: updated formset
    """
    if button_data == "add":
        return _add_new_column(form_data, formset)

    if button_data.isdigit():
        if button_data == "0":
            return formset(form_data)  # if inital formset
        return _delete_column(form_data, formset, button_data)


def _add_new_column(form_data, formset):
    column_formset = formset(form_data)
    if column_formset.is_valid():
        form_data["record-TOTAL_FORMS"] = int(form_data["record-TOTAL_FORMS"]) + 1
        column_formset = formset(form_data)
    return column_formset


def _delete_column(form_data, formset, button_data):
    """
    Deleting column form with given id
    :param button_data: Stores id of column which must be deleted
    """
    pattern = f"record-{button_data}"
    for key in form_data.copy():
        if pattern in key:
            form_data.pop(key)
    form_data["record-TOTAL_FORMS"] = int(form_data["record-TOTAL_FORMS"]) - 1
    column_formset = formset(form_data)
    return column_formset
