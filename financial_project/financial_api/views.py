from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FinancialData
from rest_framework import status
from django.db.models import Max, Min

from .serializers import FinancialDataSerializer


class FinancialMeasureListView(APIView):
    def get(self, request):
        financial_measure = request.GET.get('financial_measure')
        financial_measure_data = list(FinancialData.objects.filter(financial_measure=financial_measure).values())
        return Response(financial_measure_data)


class FinancialMeasureModelView(APIView):
    def get(self, request, pk):
        financial_measure_data = FinancialData.objects.get(id=int(pk))
        serializer = FinancialDataSerializer(financial_measure_data)
        return Response(serializer.data)

    def post(self, request):
        """Create an instance"""
        # financial_measure = request.data["financial_measure"]
        # financial_measure_data = list(FinancialData.objects.filter(financial_measure=financial_measure).values())
        # return Response(financial_measure_data)
        pass

    def patch(self, request):
        """fecha y finalmeasure"""
        """Update an element see if here es patch or put"""
        pass

    def delete(self, request,pk):
        """Delete an element"""
        FinancialData.objects.get(pk=pk).delete()


