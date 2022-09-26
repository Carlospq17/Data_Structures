from api.custom_objects.structure.Structure import Structure

class QueueStructure(Structure):

    def operation(self) -> str:
        return "{Result of the QueueStructure operation}"