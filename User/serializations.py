from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    user_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    user_confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'user_id', 'user_name', 'user_username', 'user_password',
            'user_confirm_password', 'user_email', 'user_contact'
        ]


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        style={'placeholder': 'Username', 'autofocus': True}
    )
    password = serializers.CharField(
        max_length=100,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
