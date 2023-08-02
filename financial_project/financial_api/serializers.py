from rest_framework.serializers import ModelSerializer
from .models import FinancialData

class FinancialDataSerializer(ModelSerializer):
    class Meta:
        model = FinancialData
        fields = '__all__'
