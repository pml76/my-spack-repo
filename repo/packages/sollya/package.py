# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
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
#     spack install sollya
#
# You can edit this file again by typing:
#
#     spack edit sollya
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Sollya(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://gforge.inria.fr/frs/download.php/file/37748/sollya-7.0.tar.bz2"

    version('7.0', sha256='15745871f7dd3e96e12915098dd6df2078b815853a38143b2bc6c01477044984')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on( 'mpfr' )
    depends_on( 'libxml2' )
    depends_on( 'gmp' )
    depends_on( 'mpfi' )
    depends_on( 'fplll' )
    depends_on( 'gnuplot' )


    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
