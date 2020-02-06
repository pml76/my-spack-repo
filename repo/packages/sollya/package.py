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
    url      = "file://localhost/home/peter/my-spack-repo/tars/sollya.tar.gz"

    version('7.0', sha256='fa40a17d3f837ac852f403e96b5404708601ec40e80a3ff6768e0cc008fad3c2')

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
        spec = self.spec
        args = [ "--with-fplll=%s" % spec['fplll'].prefix,
                 "--with-xml2=%s" % spec['libxml2'].prefix,
                 "--with-gmp=%s" % spec['gmp'].prefix,
                 "--with-mpfr=%s" % spec['mpfr'].prefix,
                 "--with-mpfi=%s" % spec['mpfi'].prefix ]
        return args
