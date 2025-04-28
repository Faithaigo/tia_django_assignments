from rest_framework import serializers
from .models import User


class UsersSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    email = serializers.EmailField(max_length=20, allow_blank=False)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','password','created_at']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # TODO: Figure out how to hash a password


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20, allow_blank=False)

    class Meta:
        model = User
        fields = ['full_name', 'username', 'email','password','created_at']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        read_only_fields = ['full_name','username','created_at']