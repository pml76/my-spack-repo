# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install gappa
#
# You can edit this file again by typing:
#
#     spack edit gappa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Gappa(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://gforge.inria.fr/frs/download.php/file/38044/gappa-1.3.5.tar.gz"
    # url      = "https://gforge.inria.fr/frs/download.php/file/37624/gappa-1.3.3.tar.gz"

    version('1.3.5', sha256='fc80c87f95e7141a95965807e46b50e82f20eefc6179a55c5cda1989796c3c60')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    
    depends_on( 'boost' )
    depends_on( 'gmp' )
    depends_on( 'mpfr' )

    def setup_environment(self, spack_env, run_env):
       spec = self.spec

       spack_env.append_flags('LDFLAGS', ('-L'+spec['boost'].prefix+'/lib'))
       spack_env.append_flags('CFLAGS', ('-I'+spec['boost'].prefix+'/include'))
       spack_env.append_flags('CXXFLAGS', ('-I'+spec['boost'].prefix+'/include'))

       spack_env.append_flags('LDFLAGS', ('-L'+spec['gmp'].prefix+'/lib'))
       spack_env.append_flags('CFLAGS', ('-I'+spec['gmp'].prefix+'/include'))
       spack_env.append_flags('CXXFLAGS', ('-I'+spec['gmp'].prefix+'/include'))

       spack_env.append_flags('LDFLAGS', ('-L'+spec['mpfr'].prefix+'/lib'))
       spack_env.append_flags('CFLAGS', ('-I'+spec['mpfr'].prefix+'/include'))
       spack_env.append_flags('CXXFLAGS', ('-I'+spec['mpfr'].prefix+'/include'))

    def build(self, spec, prefix):
        remake = Executable('./remake' )
        remake() 

    def install(self, spec, prefix ):
        remake = Executable('./remake' )
        remake('install') 
  
    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
