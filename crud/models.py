from django.contrib.gis.db import models
#from django.contrib.gis.db import models as gis_models


class SpatialData(models.Model):
    """A marker with name and location."""

    ADMIN = models.CharField(max_length=255, unique=True)
    ISO_A3 = models.CharField(max_length=3)
    location = models.GeometryField()

    def __str__(self):
        """Return string representation."""
        return self.ADMIN