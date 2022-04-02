from django.db import IntegrityError
from django.shortcuts import render
from datetime import date as dt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin, UpdateModelMixin

from projectifyapp.models import Project, OperationalUser, Dedication
from projectifyapp.SerializersModels import ProjectSerializer, OperationalUserSerializer, DedicationSerializerCreate, \
    DedicationSerializerList, DedicationSerializerUpdate


class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class OperationalUserView(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = OperationalUser.objects.all()
    serializer_class = OperationalUserSerializer


class DedicationView(ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Dedication.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return DedicationSerializerCreate
        elif self.action == 'update':
            return DedicationSerializerUpdate
        else:
            return DedicationSerializerList

    def create(self, request, *args, **kwargs):
        fecha = dt.fromisoformat(self.request.data['date'])
        week = fecha.isocalendar()[1]
        isoweek = f'{fecha.year}W{week}'
        if not Dedication.objects.filter(isoweek=isoweek).exists():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(isoweek=isoweek)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': 'No puedes reportar dos veces la misma semana-proyecto'})

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        fecha = instance.date
        todays_date = dt.today()
        instance.dedicacion = self.request.data['dedicacion']
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if fecha.month == todays_date.month:
            self.perform_update(serializer)
            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}
            return Response(serializer.data)
        else:
            return Response({'error': 'No puede editar dedicación fuera del mes calendario de la fecha de edición'})


