from django.urls import path

from .views import (
    CompanyListView,
    # CompanyCreateView,
    # CompanyDeleteView,
    # CompanyUpdateView,
)

urlpatterns = [
    # path('<int:pk>/edit/', CompanyUpdateView.as_view(), name='company_edit'),
    # path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='company_delete'),
    # path('new/', CompanyCreateView.as_view(), name='company_new'),
    path('', CompanyListView.as_view(), name='company_list'),
]