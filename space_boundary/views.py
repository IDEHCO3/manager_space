from rest_framework import generics
from space_boundary.models import SpaceBoundary
from serializers import SpaceBoundarySerializer
from dynamic_url.models import HierarchicalStructure

# Create your views here.
class SpaceBoundariesList(generics.ListCreateAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer

    def get_queryset(self):
        query = []

        if self.kwargs.has_key('dynamic_url'):
            query = SpaceBoundary.objects.all()
            filters_list = self.kwargs['dynamic_url'].split("/")
            hierarchical = HierarchicalStructure.objects.all().filter(name=filters_list[0])[0]
            if not hierarchical:
                return []

            for idx, filter in enumerate(filters_list):
                if idx == 0:
                    continue
                hierarchical = hierarchical.get_level_down(filter.lower())
                if not hierarchical:
                    return []

            for idx, filter in enumerate(filters_list):
                if idx == 0:
                    continue
                if idx % 2 == 1:
                    if idx != 1 and query.__len__() >= 1:
                        query = query[0]
                        query = query.col_of_children.all()
                    filter = filter.lower()
                    query = query.filter(type=filter)
                else:
                    filter = filter.upper()
                    query = query.filter(name=filter)

        return query


class SpaceBoundariesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer

class DynamicURL(generics.GenericAPIView):
    queryset = SpaceBoundary.objects.all()
    serializer_class = SpaceBoundarySerializer