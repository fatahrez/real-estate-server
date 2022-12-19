from datetime import datetime, timedelta

import jwt 

from rest_framework import generics, status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from real_estate.apps.common.utils import send_link

from real_estate.apps.users.models import User
from real_estate.apps.users.serializers import CustomTokenObtainPairSerializer, RegistrationSerializer, UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from real_estate.config.settings.base import env, SIMPLE_JWT

class RegistrationAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

    def post(self, request, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.validated_data
        serializer.save()
        res = {}

        try:
            user = User.objects.get(
                email=serializer_data.get('email')
            )
        except User.DoesNotExist:
            return Response({'error': 'user does not exist'}, status=status.HTTP_200_OK)
        
        if user.is_active:
            res.update(
                {
                    'success_message': 'Account creation was successful',
                    'status': status.HTTP_201_CREATED,
                    'refresh': user.tokens()['refresh'],
                    'access': user.tokens()['access']
                }
            )
        else:
            res.update({
                'activate account': 'please check your email to activate account'
            })
        
        return Response(res, status=res.get('status'))


class LoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = CustomTokenObtainPairSerializer


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)

        return Response(serializer.data['tokens'], status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

class SendPasswordResetEmail(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):

        try:
            input_email = request.data.get('email')

            user = User.objects.get(email=input_email)
            email = user.email

            subject = 'Password Reset'
            message = 'Your password reset request has been received'

            recipient = [email]
            payload = {
                'email': recipient,
                'iat': datetime.now(),
                'exp': datetime.utcnow() + timedelta(minutes=20)
            }
            token = jwt.encode(payload,
                            env('SECRET_KEY'),
                            algorithm='HS256')
            url = 'api/users/password/reset/'

            template = 'password_reset.html'

            kwargs = {
                "email": email,
                "subject": subject,
                "template": template,
                "url": url,
                "token": token
            }

            send_link(**kwargs)

            message = {
                "message": "email has been successfully sent",
                "token": token
            }
            return Response(message, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            message = {
                "message": "This email does not exist"
            }
        
        return Response(message, status=status.HTTP_404_NOT_FOUND)


class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)

    def put(self, request, token):
        try:
            decoded = jwt.decode(token, SIMPLE_JWT['SIGNING_KEY'],
                                algorithms=SIMPLE_JWT['ALGORITHM'])
            print(decoded)
            user = User.objects.get(id=decoded['user_id'])
            print(user)
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')

            if password == confirm_password:
                user.set_password(password)
                user.save()
            
                message = {
                    "message": "New password set"
                }
                return Response(message, status=status.HTTP_200_OK)
            else:
                message = {
                    "message": "Passwords dont match"
                }
                return Response(message, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            message = {
                'message': 'User does not exist'
            }
            return Response(message, status=status.HTTP_404_NOT_FOUND)
        except jwt.ExpiredSignatureError:
            message = {
                'message': 'Token has expired'
            }
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.InvalidSignatureError:
            message = {
                'message': 'Invalid Signature'
            }
            return Response(message, status=status.HTTP_401_UNAUTHORIZED)
        except jwt.DecodeError:
            message = {
                'message': 'Unable to decode token'
            }

            return Response(message, status=status.HTTP_401_UNAUTHORIZED)