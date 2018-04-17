# bricc.py

bricc.py provides a python wrapper for using the BrIcc conversion coefficient
calculator.
It requires a working copy of briccs, the slave version of the BrIcc software. This is available from <http://bricc.anu.edu.au/>.

## Installation

The module can be installed with

python setup.py install


## Usage

First import Bricc

>>> from bricc import Bricc

Then create a Bricc object, for example for a 100 keV E2 transition in Nobelium-254.  The arguments here are those passed to briccs for the actual calculation:

>>> iccs = Bricc(102, 100, 'E2')

The conversion coefficents and electron energies can now be accessed as dicts, with an entry for each shell. For example, the total conversion coefficient is:
>>> iccs.ICC['total']
31.6

Or for just the L shell the conversion coefficent is:
>>> iccs.ICC['L']
22.6

And the elctron energy (transition energy minus K-shell binding energy):
>>> iccs.E['L']
73.91

Attempting to access values for a shell where the electron binding energy is less than the transition energy gives a KeyError:
>>> iccs.ICC['K']
Traceback (most recent call last):
    ...
KeyError: 'K'
