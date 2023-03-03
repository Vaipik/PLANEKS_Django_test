from pathlib import Path

from django.utils import timezone


def _get_folder_name(instance, filename) -> str:
    """
    Creating folder with name according to category with year, month, day additions
    :param instance: instance of django model with FileField
    :param filename:
    :return: str for FileFields upload_to
    """
    extension = Path(filename).suffix[1:]
    new_filename = f"{instance.pk}.{extension}"  # UUID.EXT
    # Will be converted in models.FileField
    date_path = timezone.now().date().strftime("%Y/%m/%d")
    path = f"{date_path}/{new_filename}"  # MEDIA/created_date/UUID.EXT
    return path
