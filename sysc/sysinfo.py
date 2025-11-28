# | 'sysinfo' |
# 'sysinfo' is a built-in command for the 'd4' operating environment project to show information about 'd4'.
# 'sysinfo' comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysifo' is in a stable development state, but expect changes in further updates.

# Importing required libraries :
import os # > used to import system details

# Importing system details :
sysdtls = os.path.join('syscnf', 'sysdtl', 'main.txt')

# Main functionality :
def main():
    with open(sysdtls, 'r') as sysdtl: # > opens 'sysdtls' as 'sysdtl'
        dtl = sysdtl.readlines() # > list every detail according to it's line
    print("- Description  :", dtl[1]) # > prints line 1 from main.txt (system's description)
    print("- Version      :", dtl[2]) # > prints line 2 from main.txt (system's version)
    print("- Code name    :", dtl[3]) # > prints line 3 from main.txt (system's version code name)
    print("- Build number :", dtl[4]) # > prints line 4 from main.txt (system's build number)
    print("- Release date :", dtl[5]) # > prints line 5 from main.txt (system's release date)
