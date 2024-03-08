from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Facility, Project, Dataset, Schema
from .serializers import (
    UserSerializer,
    GroupSerializer,
    FacilitySerializer,
    ProjectSerializer,
    DatasetSerializer,
    SchemaSerializer,
)
from .permissions import NestedPerms


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class FacilityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows facilities to be viewed or edited.
    """

    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer
    permission_classes = [NestedPerms]


class SchemaViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemaSerializer
    permission_classes = [NestedPerms]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [NestedPerms]


class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows dataset to be viewed or edited.
    """

    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [NestedPerms]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["project"]
