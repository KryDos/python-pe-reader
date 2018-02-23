import struct
from lib.helper import *

class OptionalHeaderReader():
    def __init__(self, file, header_start_addr):
        self.file = file
        self.header_point = header_start_addr
        self.isPePlus = False

    def getMagic(self):
        OFFSET = 0
        magicNumbersMap = {
            0x10b: '32 Bits',
            0x20b: '64 Bits',
        }

        self.file.seek(self.header_point + OFFSET)
        magic, = struct.unpack('h', self.file.read(2))

        if magic in magicNumbersMap:
            self.isPePlus = magicNumbersMap[magic] == magicNumbersMap[0x20b]
            return magicNumbersMap[magic]

        return 'Unknown'

    def getImageBase(self):
        OFFSET = 28
        bytesToRead = 4
        unpackId = 'i'

        if self.isPePlus:
            bytesToRead = 8
            unpackId = 'q'
            OFFSET=24

        self.file.seek(self.header_point + OFFSET)
        the_address, = struct.unpack(unpackId, self.file.read(bytesToRead))
        return str(hex(the_address))

    def getEntryPoint(self):
        OFFSET = 16
        self.file.seek(self.header_point + OFFSET)
        the_address, = struct.unpack('i', self.file.read(4))
        return str(hex(the_address))
