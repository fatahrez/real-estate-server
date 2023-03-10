from django.core.mail import send_mail
from real_estate.apps.enquiries.serializers import EnquirySerializer
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from real_estate.config.settings.base import DEFAULT_FROM_EMAIL

from .models import Enquiry


class ListAllEnquiryAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EnquirySerializer
    queryset = Enquiry.objects.all().order_by("-created_at")


class EnquiryDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, id):
        enquiry = Enquiry.objects.get(id=id)
        serializer = EnquirySerializer(enquiry)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data["subject"]
        name = data["name"]
        email = data["email"]
        message = data["message"]
        from_email = data["email"]
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(name=name, email=email, subject=subject, message=message)
        enquiry.save()

        return Response({"data": data, "success": "Your Enquiry was successfully submitted"})

    except:
        return Response({"fail": "Enquiry was not sent. Please try again"})
