from package import *

class reveal(PythonPackage):
    dependencies = ["git","libdivsufsort","seqal_python"]

    def fetch(self):
        runCommand("git clone https://github.com/jasperlinthorst/reveal.git")
    
    unpack=""
    
    workdir="reveal"
