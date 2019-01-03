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
#     spack install libpqxx
#
# You can edit this file again by typing:
#
#     spack edit libpqxx
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class Libpqxx(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.example.com"
    url      = "https://github.com/jtv/libpqxx/archive/6.2.3.zip"

    version('6.2.3', '1fae7ca1da9df91a029105e80bfe4136')
    version('6.2.2', '2f47a16db8eecf93416e1d6d5d78a2ba')
    version('6.2.1', '7ff6e10e15862f66a2982d91bb90437f')
    version('6.2.0', '16329ee5e589298ed157e31aba1725f3')
    version('6.1.1', '885f5b7f69de0d6844d0b147e3617c12')
    version('6.1.0', 'a606ab4bc0788b720cc542850334ebab')
    version('6.0.0', '33180530295ee558ff6d2821e71d1d37')
    version('5.1.1', '5274970f1a77d2b2e7722fdacef0cf31')
    version('5.1.0', '83dab5d6d261ee16822ad33ed0d40e43')
    version('5.0.1', 'b03f6f1c46d8aba0b89ea85c158e651b')

    # FIXME: Add dependencies if required.
    depends_on('postgresql')
    depends_on('xmlto')

