# | 'syscrdt' |
# 'syswlcm' is a built-in command for the 'd4' operating environment project to show the credits of 'd4'.
# 'syscrdt' comes with no license and it's totally free to use and modify, use it and it's source code wisely.
# 'syscrdt' is in a stable development state, but expect changes in further updates.

# Imports system information from 'sysdtls.py' :
from sysdtls import ver
from sysdtls import vercn
from sysdtls import rlsdate
from sysdtls import bigdes

# Main functionality :
def main():
    print("> | d4 Operating enviromment |")
    print("- Version      :", ver)
    print("- Code name    :", vercn)
    print("- Release date :", rlsdate)
    print("- Description  :", bigdes)
