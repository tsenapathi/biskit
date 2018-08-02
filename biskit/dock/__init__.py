##
## Biskit, a toolkit for the manipulation of macromolecular structures
## Copyright (C) 2004-2016 Raik Gruenberg & Johan Leckner
##
## This program is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 3 of the
## License, or any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
## General Public License for more details.
##
## You find a copy of the GNU General Public License in the file
## license.txt along with this program; if not, write to the Free
## Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
"""
Protein-protein docking related modules
"""
from biskit import EHandler

try:
    from .complex import Complex
    from .complexList import ComplexList
    from .complexModelRegistry import ComplexModelRegistry
    from .complexvc import ComplexVC
##    from ComplexVCList import ComplexVCList
##    from ComplexTraj import ComplexTraj
##    from ComplexRandomizer import ComplexRandomizer
##    from Docker import Docker
##    from FixedList import FixedList
##    from HexParser import HexParser
##    from delphiBindingEnergy import DelphiBindingEnergy

##     from Intervor import Intervor
##     from PatchGenerator import PatchGenerator
##     from PatchGeneratorFromOrbit import PatchGeneratorFromOrbit

except IOError as why:
    EHandler.warning("Couldn't import all biskit.dock modules.\n" + str(why))
