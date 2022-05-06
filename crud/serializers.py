from rest_framework_gis import serializers
from .models import SpatialData

class SpatialDataSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        geo_field = "location"
        model = SpatialData
        fields = "__all__"