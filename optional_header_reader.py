import struct
from helper import *

class OptionalHeaderReader():
    def __init__(self, file, header_start_addr):
        self.file = file
        self.header_point = header_start_addr

    def getMagic(self):
        OFFSET = 0
        magicNumbersMap = {
            0x10b: '32 Bits',
            0x20b: '64 Bits',
        }

        self.file.seek(self.header_point + OFFSET)
        magic, = struct.unpack('h', self.file.read(2))

        if magic in magicNumbersMap:
            return magicNumbersMap[magic]

        return 'Unknown'

    def getEntryPoint(self):
        OFFSET = 16
        self.file.seek(self.header_point + OFFSET)
        the_address, = struct.unpack('i', self.file.read(4))
        return str(hex(the_address))
