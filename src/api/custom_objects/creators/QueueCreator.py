from api.custom_objects.structure import Structure
from api.custom_objects.structure.linear.dinamic.QueueStructure import QueueStructure
from api.custom_objects.creators.Creator import Creator

class QueueCreator(Creator):
    
    def factory_method(self) -> Structure:
        return QueueStructure

