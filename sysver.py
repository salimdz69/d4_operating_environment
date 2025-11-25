# | 'sysver' |
# 'sysver' is a built-in command for the 'd4' operating environment to show the system version of 'd4'.
# 'sysver' comes with no license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysver' is in a stable development state, but expect changes in further updates.

# imports 'ver' from 'sysdtls.py' :
from sysdtls import ver

# main functionality :
def main():
    print("- Version      :", ver)
