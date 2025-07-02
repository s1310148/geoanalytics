__copyright__ = """
Copyright (C)  2022 Rage Uday Kiran

     This program is free software: you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.

     This program is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
     GNU General Public License for more details.

     You should have received a copy of the GNU General Public License
     along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import pandas as pd
from PAMI.extras.dbStats.UtilityDatabase import UtilityDatabase
from PAMI.highUtilitySpatialPattern.basic import HDSHUIM
from .abstract import PatternMiner

class HighUtilitySpatialPatternMining(PatternMiner):
    def _create_database(self):
        return UtilityDatabase(self.inputFile)

    def run(self, minUtil: int, nFile: str):
        self.miner = HDSHUIM.HDSHUIM(iFile=self.inputFile, minUtil=minUtil, nFile=nFile)
        self.miner.mine()
        self.miner.printResults()