
from django.views import View
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from check_my_baggage.models import AirlineCompany
from check_my_baggage.serializers import AirlineCompaniesSerializer, \
    AirlineCompanySerializer


class AirlinesListView(View):
    Model = AirlineCompany
    Serializer = AirlineCompaniesSerializer

    def get(self, request):
        objs = self.Model.objects.all()
        serializer = self.Serializer(objs, many=True, context={"request": request})
        return JsonResponse(serializer.data, safe=False)


class AirlineDetailView(View):
    Model = AirlineCompany
    Serializer = AirlineCompanySerializer

    def get(self, request, code):
        obj = get_object_or_404(self.Model, code=code)
        serializer = self.Serializer(obj, many=False, context={"request": request})
        return JsonResponse(serializer.data, safe=False)
