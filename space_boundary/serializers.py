from rest_framework import serializers
from space_boundary.models import SpaceBoundary
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class SpaceBoundarySerializer(GeoFeatureModelSerializer):
    class Meta:
        model = SpaceBoundary
        geo_field = "geom"