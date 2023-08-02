from django.urls import path
from . import views

urlpatterns = [
    path('financialmeasure', views.FinancialMeasureListView.as_view(), name='financial-measure'),
    path('financialmeasure/<str:pk>', views.FinancialMeasureModelView.as_view(), name='financial-measure'),
]
