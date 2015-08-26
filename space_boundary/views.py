from rest_framework import generics
from space_boundary.models import SpaceBoundary
from serializers import SpaceBoundarySerializer

# Create your views here.
class SpaceBoundariesList(generics.ListCreateAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer

    def get_queryset(self):
        query = []
        if self.kwargs.has_key('state_level'):
            filter1 = self.kwargs['state_level']
            query = SpaceBoundary.objects.filter(type=filter1)

        if self.kwargs.has_key('state_name'):
            filter1_name = self.kwargs['state_name']
            query = query.filter(name=filter1_name)

        if self.kwargs.has_key('municipio_level'):
            if query.__len__() == 0:
                return []
            else:
                query = query[0]
            filter2 = self.kwargs['municipio_level']
            query = query.child.all().filter(type=filter2)

        if self.kwargs.has_key('municipio_name'):
            filter2_name = self.kwargs['municipio_name']
            query = query.filter(name=filter2_name)

        return query


class SpaceBoundariesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer