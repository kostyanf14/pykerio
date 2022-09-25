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


class TestCase_LoginType(unittest.TestCase):
    def test_00_LoginType_LoginRegular(self):
        """
        Test LoginType with LoginRegular
        """
        value = pykerio.enums.LoginType(name='LoginRegular')
        self.assertEqual(value.dump(), 'LoginRegular')
        self.assertEqual(value.get_name(), 'LoginRegular')
        self.assertEqual(value.get_value(), 0)

    def test_01_LoginType_LoginAutomatic(self):
        """
        Test LoginType with LoginAutomatic
        """
        value = pykerio.enums.LoginType(name='LoginAutomatic')
        self.assertEqual(value.dump(), 'LoginAutomatic')
        self.assertEqual(value.get_name(), 'LoginAutomatic')
        self.assertEqual(value.get_value(), 1)

    def test_02_LoginType_LoginReactivation(self):
        """
        Test LoginType with LoginReactivation
        """
        value = pykerio.enums.LoginType(name='LoginReactivation')
        self.assertEqual(value.dump(), 'LoginReactivation')
        self.assertEqual(value.get_name(), 'LoginReactivation')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_LoginType_FAIL(self):
        """
        Test LoginType with FAIL
        """
        value = pykerio.enums.LoginType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)