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
#     spack install mpfi
#
# You can edit this file again by typing:
#
#     spack edit mpfi
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Mpfi(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    svn = "https://scm.gforge.inria.fr/anonscm/svn/mpfi/"

    version('develop')

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on( 'gmp' )
    depends_on( 'mpfr' )

    depends_on( 'm4')
    depends_on( 'libtool' )
    depends_on( 'automake' )
    depends_on( 'autoconf' )
    depends_on( 'texinfo' )


    @property
    def configure_directory(self):
        return self.stage.source_path+"/trunk/mpfi"

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        spec = self.spec
        args = [ "--with-mpfr=%s" % spec['mpfr'].prefix,
                 "--with-gmp=%s" % spec['gmp'].prefix ]
        return args

