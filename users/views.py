from rest_framework import generics
from .serializers import UsersSerializer, LoginSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status



class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            if User.objects.filter(email=request.data['email']).exists():
                user = User.objects.get(email=request.data['email'])
                token, created = Token.objects.get_or_create(user=user)
                return Response({
                    'token': token.key,
                    'id': user.pk,
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name':user.last_name
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "User doesn't exist"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
