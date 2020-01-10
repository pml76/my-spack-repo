from spack import *
import os


class Pricer(CMakePackage):

    homepage = ""
    url = ""

    version('development', git='https://github.com/pml76/Pricer.git', 
             branch='master')

    extends('python')

    # Add RPATHs to this package. It should work without having to 
    # relay on the environment.
    transitive_rpaths = True

    depends_on('openssl')

    depends_on('intel-mkl')
    depends_on('arblib')
    depends_on('gmp')
    depends_on('mpfr')
    depends_on('erfa')
    depends_on('boost +python +mpi')
    depends_on('hdf5 +cxx +hl +szip +mpi')
    depends_on('intel-tbb')
    depends_on('cmake')
    depends_on('doxygen +graphviz')
    depends_on('catch2')
    depends_on('trompeloeil')
    depends_on('googlebenchmark')
    depends_on('gsl')
    depends_on('sleef')
    depends_on('vc')
    depends_on('ccache')
    depends_on('nasm')

    # use compiler and debugger supplied by spack
    # depends_on('gcc languages="c,c++,go,jit,lto,fortran"')
    depends_on('llvm')

    def cmake_args(self):
        spec = self.spec
        options = []
        options.extend(['BOOST_DIR=%s' % spec['boost'].prefix])
        return options


