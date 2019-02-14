from spack import *
import os


class Vortex(CMakePackage):

    homepage = ""
    url = ""

    version('development', git='file://localhost/home/VortexUser/Projects/RootVortex/', 
             branch='development')

    extends('python')

    # Add RPATHs to this package. It should work without having to 
    # relay on the environment.
    transitive_rpaths = True

    # depends_on('dealii +mpi')
    # depends_on('root')
    # depends_on("openssl@1.0.2p")
    depends_on('arblib')
    depends_on('gmp')
    depends_on('mpfr')
    depends_on('erfa')
    depends_on('boost +mpi')
    depends_on('hdf5 +cxx +hl +szip +mpi')
    # depends_on('intel-tbb')
    depends_on('cmake')
    depends_on('doxygen +graphviz')
    depends_on('catch2')
    depends_on('trompeloeil')
    depends_on('gsl')
    depends_on('netcdf +parallel-netcdf +mpi')
    depends_on('netcdf-cxx4')
    # depends_on('python')
    # depends_on('py-pandas')
    # depends_on('py-xarray')
    # depends_on('py-netcdf4')
    # depends_on('py-setuptools')
    # depends_on('py-pytables')
    depends_on('r')
    depends_on('r-rcpp')
    depends_on('r-ncdf4')
    # depends_on('adios2 +adios1 +hdf5 +mpi')

    # use compiler and debugger supplied by spack
    depends_on('gcc +binutils')
    depends_on('llvm +clang')
    depends_on('gdb')


    def cmake_args(self):
        spec = self.spec
        options = []
        options.extend(['BOOST_DIR=%s' % spec['boost'].prefix])
        return options


