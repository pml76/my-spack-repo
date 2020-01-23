# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
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
#     spack install cli11
#
# You can edit this file again by typing:
#
#     spack edit cli11
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Cli11(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "https://github.com/CLIUtils/CLI11/archive/v1.8.0.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    version('1.8.0', sha256='fab4d010d5c3b0886e65f0dbe28ebccc9164e5b4d1a22ac1dc4c290cfd51d0aa')
    version('1.7.1', sha256='8504330fe68e2df0801c69f5d8debc613d774c8da74611944541cf3e47de288f')
    version('1.7.0', sha256='89da3b853386518ef7a86b27d5cd02483de6b7482b400a455686da302118b954')
    version('1.6.2', sha256='36bd9b4bad0f3dc21917e1b852ea13f1e417240efdd7187cef24f5f8700f92ff')
    version('1.6.1', sha256='a16e0ada7cad7c3346b4bd75e70995f6291f8d315f632ed251ff9d386bc34efe')
    version('1.6.0', sha256='f6b74aab81da1dc0bf719d920320b14a194a347379b805bd28e7e5e1ff55cfa8')
    version('1.5.4', sha256='ac764529fc1e02a1d4d9bbbded36837a76e64b177b3daebcb5ff1b488aa82293')
    version('1.5.3', sha256='98039c4ca81d701e15a2ccb528457f8d9d1dc0a6ebcbb816334d8da458eb3352')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    depends_on('doxygen')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = ['-DCLI11_TESTING=OFF']
        return args
