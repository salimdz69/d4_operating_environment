# | 'sysinfo' |
# 'sysinfo' is a built-in command for the 'd4' operating environment project to show information about 'd4'.
# 'sysinfo' comes with no license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysifo' is in a stable development state, but expect changes in further updates.

# Imports system information from 'sysdtls' :
from sysdtls import ver
from sysdtls import vercn
from sysdtls import bldnum
from sysdtls import rlsdate

# Main functionality :
def main():
    print("- Version      :", ver)
    print("- Code name    :", vercn)
    print("- Build        :", bldnum)
    print("- Release date :", rlsdate)
