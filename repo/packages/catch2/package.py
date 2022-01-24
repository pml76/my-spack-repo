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
#     spack install catch2
#
# You can edit this file again by typing:
#
#     spack edit catch2
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Catch2(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/catchorg/Catch2/archive/v2.2.2.zip"
 
    version('2.13.8', '78148e1a75aea786038fb8d21b9455f2')
    version('2.11.1', '5a51ffb60a578246e9e7e9879a203022')
    version('2.5.0',  '7e2fde0308b6e1116bff1922c86b16a9')
    version('2.2.2',  'a4ecf9b2acf29fe02ded85d57951b573')
    version('2.2.1',  'd1324482a68cdce904a75ae83c74ec73')
    version('2.2.0',  '400a490112888d242cd63d2f8d21cfd5')
    version('2.1.2',  '54d2785d7e5549907421e8db5c1b3817')
    version('2.1.1',  '49752bea8c72177871690ebd0da03ec6')
    version('2.1.0',  '338328b503ce0cebf0dd1929224a5703')
    version('2.0.1',  '1abca1b324b99b1631e999119b172620')
    version('1.12.2', 'a6f39ae588cd9a44e7f37aad8ae42b03')
    version('1.12.1', '0f7e888db5d5fe66d44b844c87f0d81d')
    version('1.12.0', '73c804e40e8fe3abd989bdea7000342a')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
