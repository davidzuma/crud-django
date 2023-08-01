from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FinancialData
from rest_framework import status
from django.db.models import Max, Min


class FinancialMeasureView(APIView):
    def get(self, request):
        financial_measure_query = FinancialData.objects.values_list('financial_measure').distinct()
        financial_measures = [measure[0] for measure in financial_measure_query]
        return Response(financial_measures)

    def post(self, request):
        financial_measure = request.data["financial_measure"]
        financial_measure_data = list(FinancialData.objects.filter(financial_measure=financial_measure).values())
        return Response(financial_measure_data)

