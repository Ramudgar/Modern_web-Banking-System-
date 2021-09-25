import django_filters
from profiles import models

class LoanFilter(django_filters.FilterSet):
    user_contains = django_filters.CharFilter(field_name='enter_your_user_name', lookup_expr='icontains')
    class Meta:
        model =models.Loan
        fields = []