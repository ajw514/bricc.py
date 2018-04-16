# bricc.py

bricc.py provides a python wrapper for using the BrIcc conversion coefficient
calculator.
It requires a working copy of briccs, the slave version of the BrIcc software. This is available from http://bricc.anu.edu.au/

## Installation

The module can be installed as

python setup.py install


## Usage

First import Bricc

from bricc import Bricc


Then create a Bricc object. The arguments here are those passed to briccs for the actual calculation:

iccs = Bricc(proton number, transition energy, multipolarity)


The conversion coefficents and electron enrgies can now be accessed for each shell:

conversion_coefficient = iccs.ICC[shell]

electron_energy = iccs.E[shell]

