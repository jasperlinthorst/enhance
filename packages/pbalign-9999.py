from package import *

class pbalign(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/pbalign.git")

    workdir="pbalign"

    unpack=""
