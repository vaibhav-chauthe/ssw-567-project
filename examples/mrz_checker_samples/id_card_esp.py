
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################

from mrz.checker.td1 import TD1CodeChecker

print(TD1CodeChecker("IDESPBAA000589599999999R<<<<<<\n"
                     "8001014F2501017ESP<<<<<<<<<<<7\n"
                     "ESPANOLA<ESPANOLA<<CARMEN<<<<<"))
