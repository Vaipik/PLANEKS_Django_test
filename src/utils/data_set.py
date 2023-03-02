from pathlib import Path


def _get_folder_name(instance, filename) -> str:
    """
    Creating folder with name according to category with year, month, day additions
    :param instance: instance of django model with FileField
    :param filename:
    :return: str for FileFields upload_to
    """
    extension = Path(filename).suffix[1:]
    new_filename = f"{instance.id}.{extension}"  # UUID.EXT
    # Will be converted in models.FileField
    date_path = instance.uploaded_at.date() if hasattr(instance, "uploaded_at") else timezone.now().date()
    path = f"{folder_type}/{date_path}/{new_filename}"  # MEDIA/created_date/UUID.EXT
    return path