from api.custom_objects.structure import Structure
from api.custom_objects.structure.linear.dinamic.LinkedListStructure import LinkedListStructure
from api.custom_objects.creators.Creator import Creator

class LinkedListCreator(Creator):
    
    def factory_method(self) -> Structure:
        return LinkedListStructure

