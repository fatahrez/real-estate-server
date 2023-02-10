from django.urls import path

from .views import AgentListAPIView, AgentRetrieveAPIView, GetProfileAPIView, UpdateProfileAPIView

urlpatterns = [
    path("profile/me/", GetProfileAPIView.as_view(), name="get_profile"),
    path(
        "profile/update/<str:username>/",
        UpdateProfileAPIView.as_view(),
        name="update_profile",
    ),
    path("profile/agents/all/", AgentListAPIView.as_view(), name="all-agents"),
    path("profile/agents/detail/<int:id>", AgentRetrieveAPIView.as_view(), name='agent-detail'),
]
