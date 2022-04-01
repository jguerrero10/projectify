from rest_framework import serializers

from projectifyapp.models import Project, OperationalUser


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OperationalUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationalUser

        fields = [
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
