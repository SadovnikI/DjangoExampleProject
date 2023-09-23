import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Default user model extended with card_number and pin_code fields
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    card_number = models.CharField(max_length=16)
    pin_code = models.CharField(max_length=4)
