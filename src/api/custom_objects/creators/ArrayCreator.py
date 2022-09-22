from api.custom_objects.structure import Structure
from api.custom_objects.structure.linear.static.ArrayStructure import ArrayStructure
from api.custom_objects.creators.Creator import Creator

class ArrayCreator(Creator):
    
    def factory_method(self) -> Structure:
        return ArrayStructure

