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
#     spack install benchmark
#
# You can edit this file again by typing:
#
#     spack edit benchmark
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Googlebenchmark(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/google/benchmark/archive/v1.4.1.zip"

    version('1.4.1', sha256='61ae07eb5d4a0b02753419eb17a82b7d322786bb36ab62bd3df331a4d47c00a7')
    version('1.4.0', sha256='7f5f3608c9228fa023151a4b54e91f4ada4b7b49c26facede6c5b8b83ddbedad')
    version('1.3.0', sha256='51c2d2d35491aea83aa6121afc4a1fd9262fbd5ad679eb5e03c9fa481e42571e')
    version('1.2.0', sha256='cc463b28cb3701a35c0855fbcefb75b29068443f1952b64dd5f4f669272e95ea')
    version('1.1.0', sha256='3f5321836cf531e621e0187ccbb1d836cd909994ed00c102a41385cbc1254e4e')
    version('1.0.0', sha256='5560358bf31e0478fa052de10c353cff809b8d2352bdfe695887e410ec593044')

    # FIXME: Add dependencies if required.
    depends_on('googletest +gmock')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DCMAKE_BUILD_TYPE=RELEASE', 
                '-DCMAKE_POSITION_INDEPENDENT_CODE=ON']
        return args
