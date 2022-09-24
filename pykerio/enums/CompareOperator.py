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

from . import BaseEnumeration


class CompareOperator(BaseEnumeration):
    EQ = 0
    NOT_EQ = 1
    LESS_THAN = 2
    GREATER_THAN = 2
    LESS_EQ = 4
    GREATER_EQ = 5
    LIKE = 6

    VALUES = {
        'Eq': EQ,
        'NotEq': NOT_EQ,
        'LessThan': LESS_THAN,
        'GreaterThan': GREATER_THAN,
        'LessEq': LESS_EQ,
        'GreaterEq': GREATER_EQ,
        'Like': LIKE
    }
