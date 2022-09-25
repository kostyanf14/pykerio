##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018-2022 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import unittest

import pykerio


class TestCase_DynamicDnsAddressType(unittest.TestCase):
    def test_00_DynamicDnsAddressType_DynamicDnsAdressIface(self):
        """
        Test DynamicDnsAddressType with DynamicDnsAdressIface
        """
        value = pykerio.enums.DynamicDnsAddressType(name='DynamicDnsAdressIface')
        self.assertEqual(value.dump(), 'DynamicDnsAdressIface')
        self.assertEqual(value.get_name(), 'DynamicDnsAdressIface')
        self.assertEqual(value.get_value(), 0)

    def test_01_DynamicDnsAddressType_DynamicDnsAdressDetect(self):
        """
        Test DynamicDnsAddressType with DynamicDnsAdressDetect
        """
        value = pykerio.enums.DynamicDnsAddressType(name='DynamicDnsAdressDetect')
        self.assertEqual(value.dump(), 'DynamicDnsAdressDetect')
        self.assertEqual(value.get_name(), 'DynamicDnsAdressDetect')
        self.assertEqual(value.get_value(), 1)

    def test_02_DynamicDnsAddressType_DynamicDnsAdressCustom(self):
        """
        Test DynamicDnsAddressType with DynamicDnsAdressCustom
        """
        value = pykerio.enums.DynamicDnsAddressType(name='DynamicDnsAdressCustom')
        self.assertEqual(value.dump(), 'DynamicDnsAdressCustom')
        self.assertEqual(value.get_name(), 'DynamicDnsAdressCustom')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_DynamicDnsAddressType_FAIL(self):
        """
        Test DynamicDnsAddressType with FAIL
        """
        value = pykerio.enums.DynamicDnsAddressType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)