# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Sleef(CMakePackage):
    """SIMD Library for Evaluating Elementary Functions,
    vectorized libm and DFT."""

    homepage = "http://sleef.org"
    url      = "https://github.com/shibatch/sleef/archive/3.2.tar.gz"

    version('3.4.1', sha256='25babe83b9358817ac05bbec09b7557439e4e96b907b86717906e6d980ff2036')
