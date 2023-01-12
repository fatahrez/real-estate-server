from django_countries.serializer_fields import CountryField
from rest_framework import serializers

from real_estate.apps.ratings.serializers import RatingSerializer

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source="user.username")
    first_name = serializers.CharField(source="user.first_name")
    email = serializers.EmailField(source="user.email")
    country = CountryField(name_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = [
            "username",
            "first_name",
            "email",
            "id",
            "phone_number",
            "profile_photo",
            "about_me",
            "license",
            "gender",
            "country",
            "city",
            "rating",
            "num_reviews",
            "reviews",
        ]

    def get_reviews(self, obj):
        reviews = obj.agent_review.all()
        serializer = RatingSerializer(reviews, many=True)
        return serializer.data


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "license",
            "gender",
            "country",
            "city",
        ]
