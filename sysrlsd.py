# | 'sysrlsd' utility |
# 'sysrlsd' is a built-in command for the 'd4' operating environment to show the system release date of 'd4'.
# 'sysrlsd' comes with no licnese and it's totally free to use and modify, use it and it's source code wisely.
# 'sysrlsd' is in a stable development state, but expect changes in further updates.

# imports 'rlsdate' from 'sysdtls.py' :
from sysdtls import rlsdate

# main functionality :
def main():
    print(rlsdate)
