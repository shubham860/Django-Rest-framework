from rest_framework import serializers
from api.models import employee

class employeeSerializer(serializers.ModelSerializer):

	class Meta:
		model = employee
		fields = ('firstname','lastname')