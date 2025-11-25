# | 'sysbldn' |
# 'syswlcm' is a built-in command for the 'd4' operating environment project to show the build number of 'd4'.
# 'sysbldn' comes with no license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysbldn' is in a stable development state, but expect changes in further updates.

# Imports 'bldnum' from 'sysdtls' :
from sysdtls import bldnum

# Main functionality :
def main():
    print("- Build        :", bldnum)
