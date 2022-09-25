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

from pykerio.enums.interface_group_type import InterfaceGroupType
from pykerio.enums.port_assignment_type import PortAssignmentType
from pykerio.enums.wifi_encryption_type import WifiEncryptionType
from pykerio.structs.base_struct import BaseStruct
from pykerio.types.kid import KId


class WifiSsidConfig(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'id': KId,
                                   'enabled': bool,
                                   'assignment': PortAssignmentType,
                                   'ssid': str,
                                   'group': InterfaceGroupType,
                                   'encryption': WifiEncryptionType,
                                   'wpaPassword': str},
                            data=data)
