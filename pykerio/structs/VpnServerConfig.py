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

from . import BaseStruct

from ..lists.VpnRouteList import VpnRouteList

from ..structs.IdReference import IdReference
from ..structs.OptionalString import OptionalString

from ..types.IpAddress import IpAddress


class VpnServerConfig(BaseStruct):
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'kerioVpnEnabled': bool,
                                   'kerioVpnCertificate': IdReference,
                                   'port': int,
                                   'defaultRoute': bool,
                                   'ipsecVpnEnabled': bool,
                                   'mschapv2Enabled': bool,
                                   'ipsecVpnCertificate': IdReference,
                                   'cipherIke': str,
                                   'cipherEsp': str,
                                   'useCertificate': bool,
                                   'psk': OptionalString,
                                   'routes': VpnRouteList,
                                   'network': IpAddress,
                                   'mask': IpAddress,
                                   'localDns': bool,
                                   'primaryDns': IpAddress,
                                   'secondaryDns': IpAddress,
                                   'autodetectDomainSuffix': bool,
                                   'domainSuffix': str,
                                   'localWins': bool,
                                   'primaryWins': IpAddress,
                                   'secondaryWins': IpAddress},
                            data=data)
