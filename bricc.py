"""
Get ICCs from BrIcc (http://bricc.anu.edu.au/).

Requires a working copy of briccs, the slave version of the BrIcc software.

"""

from __future__ import print_function

import subprocess
import xml.etree.ElementTree as ET

from uncertainties import ufloat


class Bricc(object):

    """Output from a query to BrIcc."""

    def __init__(self, Z, E_gamma, L, delta=False):
        """
        Run briccs to get conversion coefficient data.

        Arguments:
        Z = atomic number
        E_gamma = gamma transition energy
        L = gamma transition multipolarity

        """
        self.Z = Z
        try:
            # if E_gamma is a ufloat from the uncertainties module
            self.E_gamma = ufloat(E_gamma.n, E_gamma.s)
        except:
            self.E_gamma = ufloat(E_gamma, 0.)
        self.multipolarity = L.upper()
        self.dataset = 'BrIccFO'  # this is the default for BrIcc anyway

        # BrIcc arguments must not be longer than 8 characters,
        # this includes decimal points and minus signs
        if self.E_gamma.s:
            # Count decimal places in nominal energy and scale error
            # because BrIcc wants it in nuclear data sheets format.
            decimal_places = len(str(E_gamma.n).split('.')[-1])
            nuc_err = E_gamma.s * 10**decimal_places
            self.args = ('-Z {0} -g {1:7g} -e {2:.0f} -L {3} -w {4} '
                          '-a'.format(Z, self.E_gamma.n, nuc_err,
                                      self.multipolarity, self.dataset))
        else:
            self.args = '-Z {0} -g {1:7g} -L {2} -w {3} -a'.format(
                Z, self.E_gamma.n, self.multipolarity,
                self.dataset)
        if delta:
            self.delta = delta
            self.args += ' -d {0:.5g}'.format(delta)

        self.xml = subprocess.Popen(['briccs', self.args],
                                    stdout=subprocess.PIPE).communicate()[0]
        try:
            self._xml_root = ET.fromstring(self.xml)
        except ET.ParseError:
            print('BrIcc Error')
            print(self.xml)
            print('BrIcc was run with arguments:')
            print(self.args)
            print()
            return

        xml_pureCCs = self._xml_root.findall('PureCC')
        xml_mixedCCs = self._xml_root.findall('MixedCC')
        self.ICC = {}
        self.E = {}
        self.shells = []
        for pureCC in xml_pureCCs:
            shell_name = self._shell_name(pureCC.attrib['Shell'])
            self.shells.append(shell_name)
            if '/' in shell_name:
                # ratio between two shells
                pass
            else:
                try:
                    self.ICC[shell_name] = float(pureCC.text.strip())
                except ValueError:
                    pass
                try:
                    self.E[shell_name] = float(pureCC.attrib['Eic'])
                except KeyError:
                    # No energy (total conversion coefficient)
                    pass
        for mixedCC in xml_mixedCCs:
            shell_name = self._shell_name(mixedCC.attrib['Shell'])
            self.shells.append(shell_name)
            if '/' in shell_name:
                # ratio between two shells
                pass
            else:
                try:
                    self.ICC[shell_name] = float(mixedCC.text.strip())
                except ValueError:
                    pass
                try:
                    self.E[shell_name] = float(mixedCC.attrib['Eic'])
                except KeyError:
                    # No energy (total conversion coefficient)
                    pass

    def __repr__(self):
        return '<Bricc({0}, {1}, {2})>'.format(
            self.Z, self.E_gamma, self.multipolarity)

    def __str__(self):
        return '<BrIcc: Z={0}, {1} keV, {2}>'.format(
            self.Z, self.E_gamma, self.multipolarity)

    def print_xml(self):
        print(self.xml)

    def pprint(self):
        """Print data to the terminal."""

        print('Shell\tE /keV\tICC')
        for shell in self.shells:
            if shell == 'total':
                print('{0}\t\t{1}'.format(shell, self.ICC[shell]))
            else:
                try:
                    print('{0}\t{1}\t{2}'.format(shell, self.E[shell],
                                                 self.ICC[shell]))
                except KeyError:
                    pass

    def _shell_name(self, bricc_name):
        """Format names of shells."""
        if bricc_name == 'Tot':
            return 'total'
        else:
            return bricc_name.strip('-tot')
