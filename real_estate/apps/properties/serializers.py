from pyexpat import model
from django_countries.serializer_fields import CountryField
from real_estate.apps.users.serializers import UserShortSerializer
from real_estate.apps.profiles.serializers import ProfileSerializer
from rest_framework import serializers

from .models import Property, PropertyListing, PropertyViews, NewProject, NewProjectViews


class PropertySerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    country = CountryField(name_only=True)
    cover_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    photo1 = serializers.SerializerMethodField()
    photo2 = serializers.SerializerMethodField()
    photo3 = serializers.SerializerMethodField()
    photo4 = serializers.SerializerMethodField()

    class Meta:
        model = Property
        fields = [
            "id",
            "user",
            "profile_photo",
            "title",
            "slug",
            "ref_code",
            "description",
            "country",
            "city",
            "postal_code",
            "street_address",
            "property_number",
            "price",
            "plot_area",
            "total_floors",
            "bedrooms",
            "bathrooms",
            "advert_type",
            "property_type",
            "cover_photo",
            "photo1",
            "photo2",
            "photo3",
            "photo4",
            "published_status",
            "views",
        ]

    # def get_user(self, obj):
    #     return obj.user.username

    def get_cover_photo(self, obj):
        return obj.cover_photo.url

    def get_photo1(self, obj):
        return obj.photo1.url

    def get_photo2(self, obj):
        return obj.photo2.url

    def get_photo3(self, obj):
        return obj.photo3.url

    def get_photo4(self, obj):
        return obj.photo4.url

    def get_profile_photo(self, obj):
        return obj.user.profile.profile_photo.url


class PropertyCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = Property
        exclude = ["updated_at"]


class PropertyViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyViews
        exclude = ["updated_at"]

class PropertyListingSerializer(serializers.ModelSerializer):
    agent = ProfileSerializer(source='agent.profile', read_only=True)
    property = PropertySerializer()

    class Meta:
        model = PropertyListing
        fields = [
            "id",
            "agent",
            "property"
        ]
    

class PropertyListingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyListing
        exclude = ["updated_at"]

class NewProjectSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)
    cover_photo = serializers.SerializerMethodField()
    profile_photo = serializers.SerializerMethodField()
    photo1 = serializers.SerializerMethodField()
    photo2 = serializers.SerializerMethodField()

    class Meta:
        model = NewProject
        fields = [
            "id",
            "user",
            "profile_photo",
            "name",
            "slug",
            "location",
            "ref_code",
            "description",
            "country",
            "city",
            "price",
            "square_feet",
            "bedrooms",
            "bathrooms",
            "property_type",
            "construction_status",
            "completion_date",
            "cover_photo",
            "photo1",
            "photo2",
            "published_status",
            "views"
        ]

    def get_cover_photo(self, obj):
        return obj.cover_photo.url
    
    def get_photo1(self, obj):
        return obj.photo1.url
    
    def get_photo2(self, obj):
        return obj.photo2.url
    
    def get_profile_photo(self, obj):
        return obj.user.profile.profile_photo.url


class NewProjectCreateSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True)

    class Meta:
        model = NewProject
        exclude = ["updated_at"]


class NewProjectViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewProjectViews
        exclude = ["updated_at"]