from django.urls import path
from . import views

urlpatterns = [
    path('financialmeasure', views.FinancialMeasureView.as_view()),
]