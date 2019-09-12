from datetime import datetime

from rest_framework import generics
from rest_framework.response import Response

from .serializers import *


class CityViewSet(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class CityDetail(generics.RetrieveAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class CityCreateView(generics.CreateAPIView):
    serializer_class = CitySerializer

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class StreetViewSet(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        queryset = Street.objects.all()
        city_id = self.kwargs['city_id']
        if city_id is not None:
            queryset = queryset.filter(city_id=city_id)
        return queryset

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class StreetCreateView(generics.CreateAPIView):
    serializer_class = StreetSerializer

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class ShopCreateView(generics.CreateAPIView):
    serializer_class = ShopSerializer

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)


class ShopViewSet(generics.ListAPIView):
    serializer_class = ShopSetSerializer

    def get_queryset(self):
        print(self.request.query_params)
        queryset = Shop.objects.all()

        city_name = self.request.query_params.get('city', None)
        if city_name is not None:
            queryset = queryset.filter(city_name=city_name)

        street_name = self.request.query_params.get('street', None)
        if street_name is not None:
            queryset = queryset.filter(street_name=street_name)
        isopen = self.request.query_params.get('open', None)
        if isopen is not None:
            dt = datetime.now().time()
            open_shops = queryset.filter(work_from__lt=dt).filter(
                work_to__gt=dt)
            if isopen == '1':
                queryset = open_shops
            elif isopen == '0':
                queryset = queryset.exclude(id__in=open_shops)

        return queryset

    def handle_exception(self, exc):
        return Response({'data': 'Bad request'}, status=400)
