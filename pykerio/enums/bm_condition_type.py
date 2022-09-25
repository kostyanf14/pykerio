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

from pykerio.enums.base_enumeration import BaseEnumeration


class BMConditionType(BaseEnumeration):
    BMConditionTrafficType = 0
    BMConditionQuota = 1
    BMConditionLargeData = 2
    BMConditionTrafficRule = 3
    BMConditionContentRule = 4
    BMConditionService = 5
    BMConditionDscp = 6
    BMConditionUsers = 7
    BMConditionInvalid = 8
    BMContentRuleType = 9
    BMConditionGuests = 10
    BMConditionApplication = 11
