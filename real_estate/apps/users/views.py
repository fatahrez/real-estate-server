from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from real_estate.apps.users.models import User
from real_estate.apps.users.serializers import CustomTokenObtainPairSerializer, RegistrationSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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

