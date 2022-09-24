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


class TestCase_CollisionList(unittest.TestCase):
    def test_01_CollisionList(self):
        """
        Test CollisionList
        """
        testlist = pykerio.lists.CollisionList()
        self.assertEquals(len(testlist), 0)

        rule1 = pykerio.types.KId('rule1')
        idref1 = pykerio.structs.IdReference({'id': rule1,
                                              'name': 'Rule 1',
                                              'invalid': False})
        rule2 = pykerio.types.KId('rule2')
        idref2 = pykerio.structs.IdReference({'id': rule2,
                                              'name': 'Rule 2',
                                              'invalid': False})
        teststruct = pykerio.structs.Collision({
            'rule': idref1,
            'overlappedRule': idref2})
        testlist.append(teststruct)
        self.assertEquals(len(testlist), 1)
        self.assertEquals(testlist[-1], teststruct)

        testlist.clear()
        self.assertEquals(len(testlist), 0)
