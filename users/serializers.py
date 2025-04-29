from rest_framework import serializers
from django.contrib.auth.models import User

class UsersSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20, allow_blank=False)

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

    # TODO: Figure out how to hash a password


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20, allow_blank=False)

    class Meta:
        model = User
        fields = ['id','first_name','last_name', 'username', 'email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }
        read_only_fields = ['first_name','last_name','username']