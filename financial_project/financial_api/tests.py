from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FinancialData
from .serializers import FinancialDataSerializer


class FinancialMeasureDataViewTest(APITestCase):
    def setUp(self):
        self.financial_data = FinancialData.objects.create(
            financial_measure="Revenue",
            date="2023-08-02T12:00:00Z",
            amount=1000.0,
            currency="USD",
            unit="Million"
        )

    def test_get_financial_measure_data_missing_param(self):
        url = reverse('financial-measure')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_financial_measure_data_invalid_param(self):
        url = reverse('financial-measure')
        response = self.client.get(url, {'financial_measure': 'NonExistentMeasure'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)


class FinancialMeasureModelViewTest(APITestCase):
    def setUp(self):
        self.financial_data = FinancialData.objects.create(
            financial_measure="Revenue",
            date="2023-08-02T12:00:00Z",
            amount=1000.0,
            currency="USD",
            unit="Million"
        )
        self.url = reverse('financial-measure', kwargs={'pk': self.financial_data.pk})

    def test_get_financial_measure_data(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = FinancialDataSerializer(self.financial_data).data
        self.assertEqual(response.data, expected_data)

    def test_get_financial_measure_data_not_found(self):
        url = reverse('financial-measure', kwargs={'pk': 99999})  # Non-existent pk
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_patch_financial_measure_data(self):
        data_to_update = {
            "amount": 1500.0
        }
        response = self.client.patch(self.url, data_to_update)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.financial_data.refresh_from_db()
        self.assertEqual(self.financial_data.amount, 1500.0)

    def test_patch_financial_measure_data_not_found(self):
        url = reverse('financial-measure', kwargs={'pk': 99999})  # Non-existent pk
        data_to_update = {
            "amount": 1500.0
        }
        response = self.client.patch(url, data_to_update)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_financial_measure_data(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FinancialData.objects.filter(pk=self.financial_data.pk).exists())

    def test_delete_financial_measure_data_not_found(self):
        url = reverse('financial-measure', kwargs={'pk': 99999})  # Non-existent pk
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
