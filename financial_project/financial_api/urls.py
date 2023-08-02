from django.urls import path
from . import views

urlpatterns = [
    path('financialmeasures', views.FinancialMeasuresListView.as_view(), name='financial-measure'),
    path('financialmeasure', views.FinancialMeasureDataView.as_view(), name='financial-measure'),
    path('financialmeasure/<str:pk>', views.FinancialMeasureModelView.as_view(), name='financial-measure'),
]
