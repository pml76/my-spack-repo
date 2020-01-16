##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install trompeloeil
#
# You can edit this file again by typing:
#
#     spack edit trompeloeil
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Trompeloeil(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/rollbear/trompeloeil/archive/v32.zip"
    
    version('36', '6a0f5de53e897aa038d50e06569d7c77')
    version('32', 'a4b6d352d9d512c77f62fbde7c53788a')
    version('31', 'f2243bb8773a24da4dea0f40fe97bf14')
    version('30', '1b6688116e7d474ca6d27a5c0396d1ca')
    version('29', '95ffc3b7acebfa4ee9d0b22015d7e2e5')
    version('28', '4f4f82f8835756eeb88b776a46cec5a9')
    version('27', '7fe3b655ea712b449d90ed023c728428')
    version('26', '8b579e757236c579513e98ccf0925f60')
    version('25', '1c89be58df90d561630450a96fc4dd70')
    version('24', '54ad5f29a9bbd488dffda4134e1b2a77')
    version('23', 'ca17d28004ed84b8acc4e69db85fe9d9')
    version('22', '30eb9d9e4b07e16a021b1f06827dacf0')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
