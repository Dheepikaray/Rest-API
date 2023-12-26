from rest_framework import serializers

from rest_api.models import Employee


class Emp_serializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name','emp_id')
