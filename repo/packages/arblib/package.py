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
#     spack install arb
#
# You can edit this file again by typing:
#
#     spack edit arb
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Arblib(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.arblib.org"
    url      = "https://github.com/fredrik-johansson/arb/archive/2.15.1.tar.gz"

    version('2.15.1', sha256='cb4a0cee3da56492ef3bf110fa0a1df60c58384bfcd52dd7ea7ac3d8472e21bd')
    version('2.15.0', sha256='086dd2e80232d4068ad2e5a0c560d35b13e051d75e36b6318ada88f73ffb9a7e')
    version('2.14.0', sha256='bdd28aeea8be133a3a1971bd836d2a5b946cd4dd0c0c695188bd03d1ec119959')
    version('2.13.0', sha256='d075116d094bfda96f9c4ce10bb9bf23b333a8246f48c532427168d0f91b7788')
    version('2.12.0', sha256='346af6a69118ebc6535c24b1d31055d315bab026dd24059c262a5fbcfaec6748')
    version('2.11.1', sha256='de37f008fd154bd4b9c3fd7f5b0f13928cd109358d01959a98245fe33d08bf63')

    depends_on('flint')
    depends_on('mpfr')
    depends_on('gmp')


    def install(self, spec, prefix):
        options = []
        options = [ "--prefix=%s" % prefix,
                    "--with-gmp=%s" % spec['gmp'].prefix,
                    "--with-mpfr=%s" % spec['mpfr'].prefix,
                    "--with-flint=%s" % spec['flint'].prefix ]
        configure(*options)

        make()
        if self.run_tests:
            make("check")
        make('install')
