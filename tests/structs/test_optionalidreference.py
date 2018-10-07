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

import pykerio.structs


class TestCase_OptionalIdReference(unittest.TestCase):
    def test_01_OptionalIdReference(self):
        """
        Test OptionalIdReference
        """
        enabled = True
        kid = pykerio.types.KId('user1')
        name = 'User 1'
        idref = pykerio.structs.IdReference({'id': kid,
                                             'name': name,
                                             'invalid': False})
        teststruct = pykerio.structs.OptionalIdReference({'enabled': enabled,
                                                          'value': idref})
        self.assertEquals(len(teststruct.keys()), 2)
        self.assertEquals(len(teststruct.values()), 2)

        self.assertEquals(teststruct['enabled'], enabled)
        self.assertEquals(teststruct['value'], idref)

        teststruct.clear()
        self.assertEquals(len(teststruct.keys()), 0)
