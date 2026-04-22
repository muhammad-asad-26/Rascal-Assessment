# users/models.py
from django.db import models
from uuid import uuid4

class UserType(models.TextChoices):
    ADMIN = 'ADMIN', 'Admin'
    MEMBER = 'MEMBER', 'Member'

class User(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.MEMBER,
    )
    password = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'user'
