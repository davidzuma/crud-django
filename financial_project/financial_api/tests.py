from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import FinancialData


class FinancialMeasureViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.financial_measure_1 = "Revenue"
        self.financial_measure_2 = "Assets"
        self.data_1 = {
            "financial_measure": self.financial_measure_1,
            "date": "2023-08-02T12:00:00Z",
            "amount": 1000.0,
            "currency": "USD",
            "unit": "Million"
        }
        self.data_2 = {
            "financial_measure": self.financial_measure_2,
            "date": "2023-08-02T12:00:00Z",
            "amount": 500.0,
            "currency": "USD",
            "unit": "Million"
        }
        FinancialData.objects.create(**self.data_1)
        FinancialData.objects.create(**self.data_2)

    def test_get_financial_measure_data(self):
        url = reverse('financial-measure', kwargs={'financial_measure': self.financial_measure_1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['financial_measure'], self.financial_measure_1)

    def test_get_nonexistent_financial_measure_data(self):
        url = reverse('financial-measure', kwargs={'financial_measure': 'NonExistentMeasure'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

    def test_get_multiple_financial_measure_data(self):
        url = reverse('financial-measure', kwargs={'financial_measure': self.financial_measure_2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['financial_measure'], self.financial_measure_2)
