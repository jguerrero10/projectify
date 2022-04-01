from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin

from projectifyapp.models import Project, OperationalUser
from projectifyapp.SerializersModels import ProjectSerializer, OperationalUserSerializer


class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class OperationalUserView(ListModelMixin, GenericViewSet):
    queryset = OperationalUser.objects.all()
    serializer_class = OperationalUserSerializer
