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


class TestCase_HistogramData(unittest.TestCase):
    def test_01_HistogramData(self):
        """
        Test HistogramData
        """
        inbound = 100000.0
        outbound = 200000.0
        teststruct = pykerio.structs.HistogramData({'inbound': inbound,
                                                    'outbound': outbound})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['inbound'], inbound)
        self.assertEquals(teststruct['outbound'], outbound)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
