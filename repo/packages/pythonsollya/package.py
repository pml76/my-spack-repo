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
#     spack install pythonsollya
#
# You can edit this file again by typing:
#
#     spack edit pythonsollya
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Pythonsollya(PythonPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://gitlab.com/metalibm-dev/pythonsollya"
    url      = "file://localhost/home/peter/my-spack-repo/tars/pythonsollya.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.0.0', '28f81cca8780b082a944e61875466909e8b1b65cdc503061ff0363114cd04a7e' )

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('py-setuptools')
    depends_on('python')
    depends_on('py-cython')
    depends_on('sollya')
    depends_on('gappa')
    depends_on('py-six')


#    def build_args(self, spec, prefix):
#        args = ['PYTHON=python3', 'PIP=pip3']
#        return args


#    def install_args(self, spec, prefix):
#        args = ['PYTHON=python3', 'PIP=pip3']
#        return args

#    def install(self, spec, prefix):
#        # FIXME: Unknown build system
#        make('PYTHON=python3', 'PIP=pip3')
#        make('install', 'PYTHON=python3', 'PIP=pip3')
