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
#     spack install flocq
#
# You can edit this file again by typing:
#
#     spack edit flocq
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Flocq(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://gforge.inria.fr/frs/download.php/file/37477/flocq-3.0.0.tar.gz"

    version('3.0.0', sha256='d61a375396a132ebcb5dfbb79011b56cbb7dea7c7d201aa2d81efbca4a9405c0')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

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
