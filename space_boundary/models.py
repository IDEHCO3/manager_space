from django.contrib.gis.db import models


# Create your models here.
class SpaceBoundary(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    geocode = models.CharField(max_length=50)
    geom = models.MultiPolygonField()

    col_of_children = models.ManyToManyField("self", through='SpaceBoundaryRelationship', symmetrical=False)

    def parents(self):
        return  [spr.parent  for  spr in self.col_of_children.all()]

    class Meta:
        db_table = '"malha_2013"."space_boundary"'

class SpaceBoundaryRelationship(models.Model):
    parent = models.ForeignKey(SpaceBoundary, db_column='parent', related_name='children')
    child = models.ForeignKey(SpaceBoundary, db_column='child', related_name='parents')

    class Meta:
        db_table = '"malha_2013"."space_boundary_space_boundary"'
