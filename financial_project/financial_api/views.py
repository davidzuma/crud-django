from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FinancialData
from rest_framework import status
from rest_framework.exceptions import ParseError
from django.db.models import Max, Min

from .serializers import FinancialDataSerializer


class FinancialMeasuresListView(APIView):
    def get(self, request):
        financial_measures = list(FinancialData.objects.values_list("financial_measure", flat=True).distinct())
        return Response(financial_measures)

    list(FinancialData.objects.values_list("financial_measure", flat=True).distinct())


class FinancialMeasureDataView(APIView):
    def get(self, request):
        financial_measure = request.GET.get('financial_measure')

        if not financial_measure:
            raise ParseError(
                "The 'financial_measure' parameter is missing or empty. You can go to http://127.0.0.1:8000/api/financialmeasures to check the different finantial measures")

        financial_measure_data = list(FinancialData.objects.filter(financial_measure=financial_measure).values())
        return Response(financial_measure_data)


class FinancialMeasureModelView(APIView):
    def get(self, request, pk):
        """retrieve the record with given pk"""
        try:
            financial_measure_data = FinancialData.objects.get(id=int(pk))
            serializer = FinancialDataSerializer(financial_measure_data)
            return Response(serializer.data)
        except FinancialData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        """Update fields of the current financial data record"""
        try:
            data_to_update = FinancialData.objects.get(pk=pk)
        except FinancialData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FinancialDataSerializer(data_to_update, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete the current record"""
        try:
            financial_data = FinancialData.objects.get(pk=pk)
            financial_data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # Success: 204 No Content
        except FinancialData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
