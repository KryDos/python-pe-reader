import sys
from lib.header_reader import HeaderReader
from lib.optional_header_reader import OptionalHeaderReader

class PeReader():
    OPTIONAL_HEADER_OFFSET = 20
    def __init__(self, file_path):
        self.file = open(file_path, "rb")
        self.headersReader = HeaderReader(self.file)
        self.headersReader.findAndSetPeHeaderLocation()

        self.optionalHeadersReader = OptionalHeaderReader(self.file, self.headersReader.pe_start + self.OPTIONAL_HEADER_OFFSET)

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def printOptionalHeader(self):
        print("\n")
        print('------- Optional Header --------')
        print("Compiled for:\t" + self.optionalHeadersReader.getMagic())
        print("Entry Point:\t" + self.optionalHeadersReader.getEntryPoint())

    def printPeHeader(self):
        print("\n")
        print('------- PE Header --------')
        print("PE header starts at:\t" + str(hex(self.headersReader.pe_start)))
        print("Machine Type:\t\t" + self.headersReader.getMachineName())
        print("Number of sections:\t" + self.headersReader.getNumberOfSections())
        print("Characteristics:\t" + self.headersReader.getCharacteristics())

if len(sys.argv) == 1:
    print("File path is required")
    exit(1)

pe_reader = PeReader(sys.argv[1]);

pe_reader.printPeHeader()

if (pe_reader.headersReader.is_executable):
    pe_reader.printOptionalHeader()
