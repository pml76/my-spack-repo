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
#     spack install fplll
#
# You can edit this file again by typing:
#
#     spack edit fplll
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Fplll(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/fplll/fplll/archive/5.2.1.zip"

    version('5.2.1',    sha256='35cdf2353dbc5456f182f2c6d0b46c2b5909c4e36ae909a990bf53484ceb09d4')
    version('5.2.0',    sha256='d6377cb706355863d6ba48213e251d4683223894492bcf4ec1c42d8217f10f42')
    version('5.1.0',    sha256='4f03be17e9055fd03fe3677b01405a618f052b6ccba4fec07b8f5b365e035ca3')
    version('5.0.3rc0', sha256='23b22aecd2a52ce8f9837f569fc95c3a8aabb88297836a8e331b13b6fd22a308')
    version('5.0.3',    sha256='d15311647de1fac92c346c0b90fc73f77ddc05e82fda1648ddd23f0aa99d5982')
    version('5.0.2',    sha256='b5f2ed19c2d3f1efc82e6915aaa4eeca6e3ebfb95085446668dc31d3e4e75fc4')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('gmp')
    depends_on('mpfr')

    # FIXME: Add additional dependencies if required.
    # depends_on('foo')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        # FIXME: Add arguments other than --prefix
        # FIXME: If not needed delete this function
        args = []
        return args
