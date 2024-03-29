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
#     spack install quantlib
#
# You can edit this file again by typing:
#
#     spack edit quantlib
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Quantlib(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/lballabio/QuantLib/archive/QuantLib-v1.28.tar.gz"

    version('1.28', sha256='0104a85e737b3451aa2782ac09ca158804c9e9c333ce74bfcdf64d47f20b7aa7')
    # version('1.18', sha256='ed60ef34d614f737db490a1408a249d6aef266fb96e700eb7ca2b7978734dc89')

    # FIXME: Add dependencies if required.
    depends_on('boost +mpi')
    depends_on('gcc +binutils')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
