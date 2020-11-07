from rest_framework import serializers
from .models import Admin


class AdminSerializer(serializers.ModelSerializer):
    admin_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)
    admin_confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Admin
        fields = [
            'admin_id', 'admin_name', 'admin_username', 'admin_password',
            'admin_confirm_password', 'admin_email', 'admin_contact'
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
