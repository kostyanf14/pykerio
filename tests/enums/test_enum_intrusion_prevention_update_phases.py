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


class TestCase_IntrusionPreventionUpdatePhases(unittest.TestCase):
    def test_00_IntrusionPreventionUpdatePhases_IntrusionPreventionUpdateOk(self):
        """
        Test IntrusionPreventionUpdatePhases with IntrusionPreventionUpdateOk
        """
        value = pykerio.enums.IntrusionPreventionUpdatePhases(name='IntrusionPreventionUpdateOk')
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateOk')
        self.assertEqual(value.get_name(), 'IntrusionPreventionUpdateOk')
        self.assertEqual(value.get_value(), 0)

    def test_01_IntrusionPreventionUpdatePhases_IntrusionPreventionUpdateError(self):
        """
        Test IntrusionPreventionUpdatePhases with IntrusionPreventionUpdateError
        """
        value = pykerio.enums.IntrusionPreventionUpdatePhases(name='IntrusionPreventionUpdateError')
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateError')
        self.assertEqual(value.get_name(), 'IntrusionPreventionUpdateError')
        self.assertEqual(value.get_value(), 1)

    def test_02_IntrusionPreventionUpdatePhases_IntrusionPreventionUpdateProgress(self):
        """
        Test IntrusionPreventionUpdatePhases with IntrusionPreventionUpdateProgress
        """
        value = pykerio.enums.IntrusionPreventionUpdatePhases(name='IntrusionPreventionUpdateProgress')
        self.assertEqual(value.dump(), 'IntrusionPreventionUpdateProgress')
        self.assertEqual(value.get_name(), 'IntrusionPreventionUpdateProgress')
        self.assertEqual(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_IntrusionPreventionUpdatePhases_FAIL(self):
        """
        Test IntrusionPreventionUpdatePhases with FAIL
        """
        value = pykerio.enums.IntrusionPreventionUpdatePhases(name='FAIL')
        self.assertEqual(value.dump(), 'FAIL')
        self.assertEqual(value.get_name(), 'FAIL')
        self.assertEqual(value.get_value(), 99)