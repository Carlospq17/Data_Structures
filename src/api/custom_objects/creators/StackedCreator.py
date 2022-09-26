from api.custom_objects.structure import Structure
from api.custom_objects.structure.linear.dinamic.StackStructure import StackStructure
from api.custom_objects.creators.Creator import Creator

class StackedCreator(Creator):
    
    def factory_method(self) -> Structure:
        return StackStructure

