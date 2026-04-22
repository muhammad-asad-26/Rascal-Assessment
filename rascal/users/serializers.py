from rest_framework import serializers
from models import UserType

class CreateUserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(max_length=255, null=False)
    email = serializers.EmailField(null=False)
    dob = serializers.DateField(blank=True, null=False)
    user_type = serializers.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.MEMBER,
    )
    password = serializers.CharField(max_length=128, null=False)

