from rest_framework import generics

from users.models import Human
from users.serializers import HumanSerializer


class HumanListCreateView(generics.ListCreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    http_method_names = ['get', 'post']


class HumanRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer
    http_method_names = ['get', 'put', 'delete']
