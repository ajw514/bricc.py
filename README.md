# bricc.py

bricc.py provides a python wrapper for using the BrIcc conversion coefficient
calculator (T. Kibédi, T.W. Burrows, M.B. Trzhaskovskaya, P.M. Davidson, C.W. Nestor, Jr. 'Evaluation of theoretical conversion coefficients using BrIcc' Nucl. Instr. and Meth. A 589 (2008) 202-229, <http://dx.doi.org/10.1016/j.nima.2008.02.051>).

The python module does no calculations itself, it just runs briccs with the required arguments and processes the output. It requires a working copy of briccs, the slave version of the BrIcc software. This is available from <http://bricc.anu.edu.au/>.

## Installation

The module can be installed with

python setup.py install


## Usage

First import Bricc

```
>>> from bricc import Bricc

```

Then create a Bricc object, for example for a 100 keV E2 transition in Nobelium-254.  The arguments here are those passed to briccs for the actual calculation:
```
>>> iccs = Bricc(102, 100, 'E2')

```

The conversion coefficients and electron energies can now be accessed as dicts, with an entry for each shell. For example, the total conversion coefficient is:
```
>>> iccs.ICC['total']
31.6

```

Or for just the L shell the conversion coefficient is:
```
>>> iccs.ICC['L']
22.6

```

Individual sub-shell conversion coefficients are also available:
```
>>> iccs.ICC['L1']
0.892

>>> iccs.ICC['L2']
13.85

>>> iccs.ICC['L3']
7.83

```

The electron energies (transition energy minus K-shell binding energy) for a shell can be accessed from iccs.E:
```
>>> iccs.E['L']
73.91

```

iccs.shells gives a complete list of available shells (plus 'total'):
```
>>> iccs.shells
['total', 'L1', 'L2', 'L3', 'L', 'M1', 'M2', 'M3', 'M4', 'M5', 'M', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'N', 'O1', 'O2', 'O3', 'O4', 'O5', 'O6', 'O7', 'O', 'P1', 'P2', 'P3', 'P', 'Q1', 'Q']

```
Note that this includes both a shell and its components sub-shells.


Attempting to access values for a shell where the electron binding energy is less than the transition energy gives a KeyError:
```
>>> iccs.ICC['K']
Traceback (most recent call last):
    ...
KeyError: 'K'

```

Calculations are also possible for mixed multipolarity transitions, using the same example as before but with a mixed E2/M1 multipolarity and mixing ratio 0.5,
```
>>> iccs = Bricc(102, 100, 'E2+M1', 0.5)
>>> iccs.ICC['total']
16.71

```
