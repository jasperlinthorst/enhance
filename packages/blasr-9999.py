from package import *

class blasr(MakePackage):
  
  dependencies=['git']
  
  def fetch(self):
      runCommand('git clone https://github.com/PacificBiosciences/blasr.git')
 
  workdir="blasr"

  config="""
        ./configure.py --shared --sub --no-pbbam HDF5_INCLUDE=%(prefix)s/include HDF5_LIB=%(prefix)s/lib
        make update-submodule
        make configure-submodule
    """

  build="""
        make build-submodule
        make blasr
    """
  install="""
        cp libcpp/alignment/libblasr.so %(prefix)s/lib
        cp libcpp/hdf/libpbihdf.so %(prefix)s/lib
        cp libcpp/pbdata/libpbdata.so %(prefix)s/lib
        cp blasr %(prefix)s/bin
    """
