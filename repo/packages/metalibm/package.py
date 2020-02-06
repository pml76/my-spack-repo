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
#     spack install metalibm
#
# You can edit this file again by typing:
#
#     spack edit metalibm
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack import *


class Metalibm(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    extends('python')

    # Add RPATHs to this package. It should work without having to 
    # relay on the environment.
    transitive_rpaths = True


    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url      = "file://localhost/home/peter/my-spack-repo/tars/metalibm.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers = ['github_user1', 'github_user2']

    # FIXME: Add proper versions and checksums here.
    version('1.0.0', '1f0088ea92fc98e4fa481c746f3f421ce723651523d1cc15b5f9b07897c1d7cd')

    # FIXME: Add dependencies if required.
    # depends_on('foo')
    depends_on('sollya')
    depends_on('gappa')

