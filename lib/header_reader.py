from lib.helper import *
from lib.pe_machine import PeMachine
import struct

class HeaderReader():
    ADDR_OF_PE_HEADER_POINTER = 0x3c
    PE_SIGNATURE_SIZE = 4;

    def __init__(self, file):
        self.file = file
        self.pe_start = 0
        self.is_executable = False

    def findAndSetPeHeaderLocation(self):
        self.file.seek(self.ADDR_OF_PE_HEADER_POINTER)
        self.pe_start, = struct.unpack('h', self.file.read(2))
        self.pe_start = self.pe_start + self.PE_SIGNATURE_SIZE # pad pe from signature to actual header

    def getMachineTypeId(self):
        OFFSET = 0
        self.file.seek(self.pe_start + OFFSET);
        signature, = struct.unpack('h', self.file.read(2));

        return signature;

    def getMachineName(self):
        return PeMachine.MACHINE_TYPES[self.getMachineTypeId()]

    def getNumberOfSections(self):
        OFFSET = 2
        self.file.seek(self.pe_start + OFFSET);
        number_of_sections, = struct.unpack('h', self.file.read(2));
        return str(number_of_sections)

    def getCharacteristics(self):
        OFFSET = 18
        flags = []
        self.file.seek(self.pe_start + OFFSET)
        bytes = self.file.read(2)
        the_ch_header, = struct.unpack('h', bytes)

        if ((the_ch_header & 0x0002)):
            if ((the_ch_header & 0x2000)):
                flags.append('DLL')
            elif ((the_ch_header & 0x0020)):
                flags.append('Can handle > 2GB addresses')
            elif ((the_ch_header & 0x1000)):
                flags.append('System file/Driver')
            else:
                self.is_executable = True
                flags.append('Executable')
        else:
            return 'not valid executable'

        return ", ".join(flags)
