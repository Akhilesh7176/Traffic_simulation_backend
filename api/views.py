from rest_framework import generics
from .models import Location, Vehicle
from .serializers import VehicleSerializer, LocationSerializer


class VehicleList(generics.ListCreateAPIView):
    serializer_class = VehicleSerializer

    def get_queryset(self):
        queryset = Vehicle.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(vehicleLocation=location)
        return queryset


class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()


class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
