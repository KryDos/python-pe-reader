from helper import *

class PeMachine():
    POINTER_TO_MACHINE_ADDR = int('0x3c', 16)
    SIZE_OF_PE_SIGNATURE = 4

    MACHINE_TYPES = {
        "0000": "Any",
        "01d3": "Matsushita AM33",
        "8664": "x64",
        "01c0": "ARM little endian",
        "aa64": "ARM64 little endian",
        "01c4": "ARM Thumb-2 little endian",
        "0ebc": "EFI byte code",
        "014c": "Intel 386 or later processors and compatible processors",
        "0200": "Intel Itanium processor family",
        "9041": "Mitsubishi M32R little endian",
        "266": "MIPS16",
        "366": "MIPS with FPU",
        "466": "MIPS16 with FPU",
        "1f0": "Power PC little endian",
        "1f1": "Power PC with floating point support",
        "166": "MIPS little endian",
        "5032": "RISC-V 32-bit address space",
        "5064": "RISC-V 64-bit address space",
        "5128": "RISC-V 128-bit address space",
        "1a2": "Hitachi SH3",
        "1a3": "Hitachi SH3 DSP",
        "1a6": "Hitachi SH4",
        "1a8": "Hitachi SH5",
        "1c2": "Thumb",
        "0169": "MIPS little-endian WCE v2"
    }

    def __init__(self, file):
        self.file = file

    def getMachineAddrPointer(self):
        self.file.seek(self.POINTER_TO_MACHINE_ADDR)
        addr_bytes = self.file.read(2)
        return sum(addr_bytes)

    def getValue(self):
        machine_addr_ptr = self.getMachineAddrPointer()
        self.file.seek(machine_addr_ptr + self.SIZE_OF_PE_SIGNATURE) # skip PE signature
        machine_type_bytes = self.file.read(2)

        return self.MACHINE_TYPES[bths_ex(machine_type_bytes)]
