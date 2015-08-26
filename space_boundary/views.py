from rest_framework import generics
from space_boundary.models import SpaceBoundary
from serializers import SpaceBoundarySerializer

# Create your views here.
class SpaceBoundariesList(generics.ListCreateAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer

class SpaceBoundariesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer