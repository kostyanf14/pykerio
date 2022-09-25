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


class TestCase_ContentEntityUrlType(unittest.TestCase):
    def test_00_ContentEntityUrlType_ContentEntityUrlWildcard(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlWildcard
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlWildcard')
        self.assertEqual(value.dump(), 'ContentEntityUrlWildcard')
        self.assertEqual(value.get_name(), 'ContentEntityUrlWildcard')
        self.assertEqual(value.get_value(), 0)

    def test_01_ContentEntityUrlType_ContentEntityUrlRegex(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlRegex
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlRegex')
        self.assertEqual(value.dump(), 'ContentEntityUrlRegex')
        self.assertEqual(value.get_name(), 'ContentEntityUrlRegex')
        self.assertEqual(value.get_value(), 1)

    def test_02_ContentEntityUrlType_ContentEntityUrlHostname(self):
        """
        Test ContentEntityUrlType with ContentEntityUrlHostname
        """
        value = pykerio.enums.ContentEntityUrlType(name='ContentEntityUrlHostname')
        self.assertEqual(value.dump(), 'ContentEntityUrlHostname')
        self.assertEqual(value.get_name(), 'ContentEntityUrlHostname')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_ContentEntityUrlType_FAIL(self):
        """
        Test ContentEntityUrlType with FAIL
        """
        value = pykerio.enums.ContentEntityUrlType(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)