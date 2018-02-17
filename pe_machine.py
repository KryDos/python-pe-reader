from helper import *

class PeMachine():
    MACHINE_TYPES = {
        0x0000: "Any",
        0x01d3: "Matsushita AM33",
        0x8664: "x64",
        0x01c0: "ARM little endian",
        0xaa64: "ARM64 little endian",
        0x01c4: "ARM Thumb-2 little endian",
        0x0ebc: "EFI byte code",
        0x014c: "Intel 386 or later processors and compatible processors",
        0x0200: "Intel Itanium processor family",
        0x9041: "Mitsubishi M32R little endian",
        0x266: "MIPS16",
        0x366: "MIPS with FPU",
        0x466: "MIPS16 with FPU",
        0x1f0: "Power PC little endian",
        0x1f1: "Power PC with floating point support",
        0x166: "MIPS little endian",
        0x5032: "RISC-V 32-bit address space",
        0x5064: "RISC-V 64-bit address space",
        0x5128: "RISC-V 128-bit address space",
        0x1a2: "Hitachi SH3",
        0x1a3: "Hitachi SH3 DSP",
        0x1a6: "Hitachi SH4",
        0x1a8: "Hitachi SH5",
        0x1c2: "Thumb",
        0x0169: "MIPS little-endian WCE v2"
    }
