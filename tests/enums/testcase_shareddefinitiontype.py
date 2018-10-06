##
#     Project: PyKerio
# Description: API for Kerio products
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2018 Fabio Castelli
#     License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#  You should have received a copy of the GNU General Public License along
#  with this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA
##

import unittest

import pykerio.enums


class TestCase_SharedDefinitionType(unittest.TestCase):
    def test_00_SharedDefinitionType_SharedDefinitionIpAddrGroup(self):
        """
        Test SharedDefinitionType with SharedDefinitionIpAddrGroup
        """
        value = pykerio.enums.SharedDefinitionType(name='SharedDefinitionIpAddrGroup')
        self.assertEquals(value.dump(), 'SharedDefinitionIpAddrGroup')
        self.assertEquals(value.get_name(), 'SharedDefinitionIpAddrGroup')
        self.assertEquals(value.get_value(), 0)

    def test_01_SharedDefinitionType_SharedDefinitionUrlGroup(self):
        """
        Test SharedDefinitionType with SharedDefinitionUrlGroup
        """
        value = pykerio.enums.SharedDefinitionType(name='SharedDefinitionUrlGroup')
        self.assertEquals(value.dump(), 'SharedDefinitionUrlGroup')
        self.assertEquals(value.get_name(), 'SharedDefinitionUrlGroup')
        self.assertEquals(value.get_value(), 1)

    def test_02_SharedDefinitionType_SharedDefinitionTimeRange(self):
        """
        Test SharedDefinitionType with SharedDefinitionTimeRange
        """
        value = pykerio.enums.SharedDefinitionType(name='SharedDefinitionTimeRange')
        self.assertEquals(value.dump(), 'SharedDefinitionTimeRange')
        self.assertEquals(value.get_name(), 'SharedDefinitionTimeRange')
        self.assertEquals(value.get_value(), 2)

    @unittest.expectedFailure
    def test_99_SharedDefinitionType_FAIL(self):
        """
        Test SharedDefinitionType with FAIL
        """
        value = pykerio.enums.SharedDefinitionType(name='FAIL')
        self.assertEquals(value.dump(), 'FAIL')
        self.assertEquals(value.get_name(), 'FAIL')
        self.assertEquals(value.get_value(), 99)
