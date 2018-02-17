import sys
from pe_machine import PeMachine
from header_reader import HeaderReader
from optional_header_reader import OptionalHeaderReader

class PeReader():
    def __init__(self, file_path):
        self.file = open(file_path, "rb")
        self.headersReader = HeaderReader(self.file)
        self.headersReader.findAndSetPeHeaderLocation()

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def printOptionalHeader(self):
        print()

    def printPeHeader(self):
        print("PE header starts at:\t" + str(hex(self.headersReader.pe_start)))
        print("Machine Type:\t" + self.headersReader.getMachineName())
        print("Number of sections:\t" + self.headersReader.getNumberOfSections())
        print("Characteristics:\t" + self.headersReader.getCharacteristics())

if len(sys.argv) == 1:
    print("File path is required")
    exit(1)

pe_reader = PeReader(sys.argv[1]);
print("\n")

pe_reader.printPeHeader()

if (pe_reader.headersReader.is_executable):
    pe_reader.printOptionalHeader()
