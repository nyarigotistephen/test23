import django_filters
from api.models import *

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields ='__all__'