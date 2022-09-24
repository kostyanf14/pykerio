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

from ..structs.LocalizableMessageParameters import LocalizableMessageParameters


class Error(BaseStruct):
    """
    Error details regarding a particular item,
    e.g. one of users that could not be updated or removed.
    """
    def __init__(self, data: dict):
        BaseStruct.__init__(self,
                            types={'inputIndex': int,
                                   'code': int,
                                   'message': str,
                                   'messageParameters': LocalizableMessageParameters},
                            data=data)
