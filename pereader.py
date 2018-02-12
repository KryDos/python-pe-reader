import sys
from pe_machine import PeMachine
from sections_count import SectionsCount

class PeReader():
    def __init__(self, file_path):
        self.file = open(file_path, "rb")

    def getMachine(self):
        machine = PeMachine(self.file)
        return machine.getValue()

    def getNumberOfSections(self):
        sections_counter = SectionsCount(self.file)
        return sections_counter.getValue()

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def printInfo(self):
        print("Machine Type:\t" + self.getMachine())
        print("Number of sections:\t" + self.getNumberOfSections())

if len(sys.argv) == 1:
    print("File path is required")
    exit(1)

pe_reader = PeReader(sys.argv[1]);
print("\n")
pe_reader.printInfo()
