from helper import *
from pe_machine import PeMachine

class SectionsCount():
    def __init__(self, file):
        self.file = file
        machine_data = PeMachine(self.file)
        pointer_to_machine_addr = machine_data.getMachineAddrPointer() + machine_data.SIZE_OF_PE_SIGNATURE
        self.pointer_to_machine_addr = pointer_to_machine_addr + 2 #skip machine data

    def getValue(self):
        self.file.seek(self.pointer_to_machine_addr);
        number_of_sections = self.file.read(2)
        return str(int(bths_ex(number_of_sections), 16))
