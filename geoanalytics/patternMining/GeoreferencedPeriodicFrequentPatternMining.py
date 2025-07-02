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
from PAMI.extras.dbStats.TemporalDatabase import TemporalDatabase
from PAMI.geoReferencedPeriodicFrequentPattern.basic import GPFPMiner
from .abstract import PatternMiner

class GeoreferencedPeriodicFrequentPatternMining(PatternMiner):
    def _create_database(self):
        return TemporalDatabase(self.inputFile)

    def run(self, minSupport: int, maxPer: int, nFile: str):
        self.miner = GPFPMiner.GPFPMiner(iFile=self.inputFile, minSup=minSupport, maxPer=maxPer, nFile=nFile)
        self.miner.mine()
        self.miner.printResults()