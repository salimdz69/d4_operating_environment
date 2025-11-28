# | 'syswlcm' |
# 'syswlcm' is a built-in one-time application for the 'd4' operating environment project to show help tips for the user at start-up.
# 'syswlcm' comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# 'syswlcm' is in a stable development state, but expect changes in further updates.

# Importing required libraries :
import os # > used to import system details

# Importing system details :
sysdtls = os.path.join('syscnf', 'sysdtl', 'main.txt')

# main functionality :
def main():
    with open(sysdtls, 'r') as sysdtl: # > opens 'sysdtls' as 'sysdtl'
            dtl = sysdtl.readlines() # > list every detail according to it's line
    print("> | 'd4' Operating enviromment |")
    print(">", dtl[0]) # > prints line 0 from main.txt (system's small description)
    print("> Run 'sysinfo' to see information of d4")
