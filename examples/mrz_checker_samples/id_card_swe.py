
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.checker.td1 import TD1CodeChecker

print(bool(TD1CodeChecker("I<SWE59000002<8198703142391<<<\n"
                          "8703145M1701027SWE<<<<<<<<<<<8\n"
                          "SPECIMEN<<SVEN<<<<<<<<<<<<<<<<")))
