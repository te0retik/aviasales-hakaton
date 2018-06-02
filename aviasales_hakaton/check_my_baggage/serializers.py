
from rest_framework import serializers

from check_my_baggage.models import AirlineCompany


class BaseAirlineCompaniesSerializer(serializers.ModelSerializer):
    icon = serializers.ImageField(use_url=True)
    image = serializers.ImageField(source='logo', use_url=True)


class AirlineCompaniesSerializer(BaseAirlineCompaniesSerializer):
    class Meta:
        model = AirlineCompany
        fields = ('code', 'name', 'icon')


class AirlineCompanySerializer(BaseAirlineCompaniesSerializer):
    class Meta:
        model = AirlineCompany
        fields = ('code', 'name', 'icon',
                  'baggage_allowance_link',
                  'carryon_max_x', 'carryon_max_y', 'carryon_max_z',
                  'baggage_3dimensions')
