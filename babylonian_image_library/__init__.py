# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2026, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
from .library.config import ImageLibraryConfig
from .library.coordinates import ImageCoordinates
from .library.core import SmartBabylonImageLibrary, BabylonianImageLibrary
from .library.generator import BabylonianImageGenerator
"""A deterministic infinite image library generator inspired by Borges' 'The Library of Babel'. 
Generate unique, deterministic images based on coordinate systems without storing image data."""

__version__ = "1.0.1"
__author__ = "Alexander Suvorov"
__email__ = "smartlegiondev@gmail.com"

__all__ = [
    "SmartBabylonImageLibrary",
    "ImageLibraryConfig",
    "ImageCoordinates",
    "BabylonianImageGenerator",
    "BabylonianImageLibrary"
]