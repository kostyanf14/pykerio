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


class TestCase_VpnRouteList(unittest.TestCase):
    def test_01_VpnRouteList(self):
        """
        Test VpnRouteList
        """
        testlist = pykerio.lists.VpnRouteList()
        self.assertEquals(len(testlist), 0)

        kid = pykerio.types.KId('Route 1')
        description = 'Route LAN'
        network = pykerio.types.IpAddress('192.168.10.0')
        netmask = pykerio.types.IpAddress('255.255.255.0')
        teststruct = pykerio.structs.VpnRoute({'id': kid,
                                               'enabled': True,
                                               'description': description,
                                               'network': network,
                                               'mask': netmask})
        testlist.append(teststruct)
        self.assertEquals(len(testlist), 1)
        self.assertEquals(testlist[-1], teststruct)

        testlist.clear()
        self.assertEquals(len(testlist), 0)
