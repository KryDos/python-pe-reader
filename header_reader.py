from helper import *
from pe_machine import PeMachine

class HeaderReader():
    ADDR_OF_PE_HEADER_POINTER = int('0x3c', 16)
    PE_SIGNATURE_SIZE = 4;

    def __init__(self, file):
        self.file = file
        self.pe_start = 0

    def findAndSetPeHeaderLocation(self):
        self.file.seek(self.ADDR_OF_PE_HEADER_POINTER)
        self.pe_start = sum(self.file.read(2)) + self.PE_SIGNATURE_SIZE

    def getMachineTypeId(self):
        OFFSET = 0
        self.file.seek(self.pe_start + OFFSET);
        signature = self.file.read(2);

        return bths_ex(signature);

    def getMachineName(self):
        return PeMachine.MACHINE_TYPES[self.getMachineTypeId()]

    def getNumberOfSections(self):
        OFFSET = 2
        self.file.seek(self.pe_start + OFFSET);
        number_of_sections = self.file.read(2);
        return str(int(bths_ex(number_of_sections), 16))

    def getCharacteristics(self):
        OFFSET = 18
        flags = []
        self.file.seek(self.pe_start + OFFSET)
        the_ch_header = sum(self.file.read(2))

        if ((the_ch_header & int('0x0002', 16)) == 0):
            if ((the_ch_header & int('0x2000', 16)) == 0):
                flags.append('DLL')
            elif ((the_ch_header & int('0x1000')) == 0):
                flags.append('System file/Driver')
            else:
                flags.append('Executable')
        else:
            return 'not valid executable'

        return ", ".join(flags)
