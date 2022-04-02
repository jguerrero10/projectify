from datetime import date as dt

from rest_framework import serializers

from projectifyapp.models import Project, OperationalUser, Dedication


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OperationalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalUser

        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email'

        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        firt_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        user = OperationalUser.objects.create_user(username=username, password=password, email=email,
                                                   first_name=firt_name, last_name=last_name)
        return user


class DedicationSerializerCreate(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    project_name = serializers.ReadOnlyField(source='project.name')
    date = serializers.DateField(write_only=True)
    isoweek = serializers.ReadOnlyField()

    class Meta:
        model = Dedication
        fields = [
            'id',
            'user',
            'project',
            'isoweek',
            'user_username',
            'project_name',
            'date',
            'dedicacion'
        ]


class DedicationSerializerList(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    project_name = serializers.ReadOnlyField(source='project.name')
    isoweek = serializers.ReadOnlyField()
    date = serializers.DateField(write_only=True)

    class Meta:
        model = Dedication
        fields = [
            'id',
            'user',
            'project',
            'user_username',
            'project_name',
            'isoweek',
            'date',
            'dedicacion'
        ]


class DedicationSerializerUpdate(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    project_name = serializers.ReadOnlyField(source='project.name')
    date = serializers.DateField(read_only=True)

    class Meta:
        model = Dedication
        fields = [
            'id',
            'user_username',
            'project_name',
            'date',
            'dedicacion'
        ]
