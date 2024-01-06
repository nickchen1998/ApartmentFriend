from django.db import models


class Status(models.TextChoices):
    PENDING = "pending"
    STARTED = "started"
    FAILURE = "failure"
    REVOKED = "revoked"
    SUCCESS = "success"
    RETRY = "retry"
