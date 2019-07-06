from houses.models import House
from houses.serializers import HouseSerializer
from rest_framework import viewsets


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer