from django.db import models

# Create your models here.
class HierarchicalStructure(models.Model):

    name = models.CharField(max_length=255)

    def levels_up(self):
        relations = HierarchicalStructureRelationship.objects.filter(hierarchical_structure=self.id)
        parents = []
        for hsr in relations:
            parents.append(hsr.hierarchical_structure_parent)

        return parents

    def levels_down(self):
        relations = HierarchicalStructureRelationship.objects.filter(hierarchical_structure_parent=self.id)
        children = []
        for hsr in relations:
            children.append(hsr.hierarchical_structure)

        return children

    def get_level_down(self, down):
        children = self.levels_down()
        for child in children:
            if child.name == down:
                return child
        return None

    def get_level_up(self, up):
        parents = self.levels_up()
        for parent in parents:
            if parent.name == up:
                return parent
        return None

    def __str__(self):
        return self.name

class HierarchicalStructureRelationship(models.Model):
    hierarchical_structure = models.ForeignKey(HierarchicalStructure, related_name='my_self')
    hierarchical_structure_parent = models.ForeignKey(HierarchicalStructure, null=True, related_name='my_parent')
