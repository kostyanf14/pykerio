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


class TestCase_UserFormatType(unittest.TestCase):
    def test_00_UserFormatType_UserFormatFL(self):
        """
        Test UserFormatType with UserFormatFL
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFL')
        self.assertEqual(value.dump(), 'UserFormatFL')
        self.assertEqual(value.get_name(), 'UserFormatFL')
        self.assertEqual(value.get_value(), 0)

    def test_01_UserFormatType_UserFormatFLU(self):
        """
        Test UserFormatType with UserFormatFLU
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFLU')
        self.assertEqual(value.dump(), 'UserFormatFLU')
        self.assertEqual(value.get_name(), 'UserFormatFLU')
        self.assertEqual(value.get_value(), 1)

    def test_02_UserFormatType_UserFormatFLD(self):
        """
        Test UserFormatType with UserFormatFLD
        """
        value = pykerio.enums.UserFormatType(name='UserFormatFLD')
        self.assertEqual(value.dump(), 'UserFormatFLD')
        self.assertEqual(value.get_name(), 'UserFormatFLD')
        self.assertEqual(value.get_value(), 2)

    def test_03_UserFormatType_UserFormatLF(self):
        """
        Test UserFormatType with UserFormatLF
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLF')
        self.assertEqual(value.dump(), 'UserFormatLF')
        self.assertEqual(value.get_name(), 'UserFormatLF')
        self.assertEqual(value.get_value(), 3)

    def test_04_UserFormatType_UserFormatLFU(self):
        """
        Test UserFormatType with UserFormatLFU
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLFU')
        self.assertEqual(value.dump(), 'UserFormatLFU')
        self.assertEqual(value.get_name(), 'UserFormatLFU')
        self.assertEqual(value.get_value(), 4)

    def test_05_UserFormatType_UserFormatLFD(self):
        """
        Test UserFormatType with UserFormatLFD
        """
        value = pykerio.enums.UserFormatType(name='UserFormatLFD')
        self.assertEqual(value.dump(), 'UserFormatLFD')
        self.assertEqual(value.get_name(), 'UserFormatLFD')
        self.assertEqual(value.get_value(), 5)

    @unittest.expectedFailure
    def test_99_UserFormatType_FAIL(self):
        """
        Test UserFormatType with FAIL
        """
        value = pykerio.enums.UserFormatType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)