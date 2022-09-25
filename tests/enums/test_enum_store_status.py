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


class TestCase_StoreStatus(unittest.TestCase):
    def test_00_StoreStatus_StoreStatusClean(self):
        """
        Test StoreStatus with StoreStatusClean
        """
        value = pykerio.enums.StoreStatus(name='StoreStatusClean')
        self.assertEqual(value.dump(), 'StoreStatusClean')
        self.assertEqual(value.get_name(), 'StoreStatusClean')
        self.assertEqual(value.get_value(), 0)

    def test_01_StoreStatus_StoreStatusModified(self):
        """
        Test StoreStatus with StoreStatusModified
        """
        value = pykerio.enums.StoreStatus(name='StoreStatusModified')
        self.assertEqual(value.dump(), 'StoreStatusModified')
        self.assertEqual(value.get_name(), 'StoreStatusModified')
        self.assertEqual(value.get_value(), 1)

    def test_02_StoreStatus_StoreStatusNew(self):
        """
        Test StoreStatus with StoreStatusNew
        """
        value = pykerio.enums.StoreStatus(name='StoreStatusNew')
        self.assertEqual(value.dump(), 'StoreStatusNew')
        self.assertEqual(value.get_name(), 'StoreStatusNew')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_StoreStatus_FAIL(self):
        """
        Test StoreStatus with FAIL
        """
        value = pykerio.enums.StoreStatus(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)