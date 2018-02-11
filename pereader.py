import sys
from pe_machine import PeMachine

class PeReader():
    def __init__(self, file_path):
        self.file = open(file_path, "rb")

    def getMachine(self):
        machine = PeMachine(self.file)
        return machine.getValue()

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

if len(sys.argv) == 1:
    print("File path is required")
    exit(1)

pe_reader = PeReader(sys.argv[1]);
print("\n")
print("Machine Type:\t" + pe_reader.getMachine())
