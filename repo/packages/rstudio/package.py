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
#     spack install rstudio
#
# You can edit this file again by typing:
#
#     spack edit rstudio
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Rstudio(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/rstudio/rstudio/archive/v1.2.679.zip"

    version('1.2.679', sha256='93ae12ac85e2c088290ec08eb51c31c2118b061528862ee6b0526d9d50418163')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('boost@:1.68.0')
    depends_on('openssl')
    depends_on('r')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ["-DRSTUDIO_TARGET=Desktop",
                "-DCMAKE_BUILD_TYPE=Release" ]
        return args
