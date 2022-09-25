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
from pykerio.enums import RestrictionKind


class TestCase_RestrictionTuple(unittest.TestCase):
    def test_01_RestrictionTuple(self):
        """
        Test RestrictionTuple
        """
        values = pykerio.lists.StringList()
        values.append('Something')
        values.append('Other')
        kind = RestrictionKind.ForbiddenNameList

        teststruct = pykerio.structs.RestrictionTuple({'name': 'restrictions',
                                                       'kind': kind,
                                                       'values': values})
        self.assertEqual(len(teststruct.keys()), 3)
        self.assertEqual(len(teststruct.values()), 3)

        self.assertEqual(teststruct['kind'], kind)
        self.assertEqual(teststruct['values'], values)

        teststruct.clear()
        self.assertEqual(len(teststruct.keys()), 0)
