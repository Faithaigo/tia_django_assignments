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


    def create(self, validated_data):
        user = User(
            full_name = validated_data['full_name'],
            username = validated_data['user_name'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user
