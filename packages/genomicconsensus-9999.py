from package import *

class genomicconsensus(PythonPackage):
    dependencies = ["git"]

    def fetch(self):
        runCommand("git clone https://github.com/PacificBiosciences/GenomicConsensus.git")

    workdir="GenomicConsensus"

    unpack=""
