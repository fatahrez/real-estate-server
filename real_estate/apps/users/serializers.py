import enum

from django.conf import settings
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import User, Individual, Seller, Agent, ProjectBuilder

class RegistrationSerializer(serializers.ModelSerializer):
    class Roles(enum.Enum):
        INDIVIDUAL = "INDIVIDUAL", "Individual"
        SELLER = "SELLER", "Seller"
        AGENT = "AGENT", "Agent"
        PROJECTBUILDER = "PROJECTBUILDER", "ProjectBuilder"
        STAFFMEMBER = "STAFFMEMBER", "StaffMember"
    
    password = serializers.CharField(
        min_length=6, max_length=100, write_only=True
    )
    roles = [role.value for role in Roles]
    type = serializers.ChoiceField(choices=roles, required=True)
    first_name = serializers.CharField(max_length=100, required=True)
    email = serializers.CharField(max_length=100, required=True,
                                validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'email', 'password', 'type',]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        type = self.validated_data['type']
        if type == 'INDIVIDUAL':
            user = Individual.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        elif type == 'SELLER':
            user = Seller.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        elif type == 'AGENT':
            user = Agent.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        elif type == 'PROJECTBUILDER':
            user = ProjectBuilder.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        else:
            user = StaffMember.objects.create(
                username=validated_data['email'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                password=validated_data['password'],
                type=type,
                is_active=True
            )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['role'] = user.type
        token['username'] = user.username

        return token


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'tokens')

        read_only_fields = ('tokens',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        
        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

class SocialAuthSerializer(serializers.Serializer):
    token = serializers.CharField(required=True, allow_blank=False)