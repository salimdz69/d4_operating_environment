# | 'sysbldn' |
# 'sysbldn' is a built-in command for the 'd4' operating environment project to show the build number of 'd4'.
# 'sysbldn' comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysbldn' is in a stable development state, but expect changes in further updates.

# Importing required libraries :
import os # > used to import system details

# Importing system details :
sysdtls = os.path.join('syscnf' ,'sysdtl', 'main.txt')

# Main functionality :
def main():
    with open(sysdtls, 'r') as sysdtl: # > opens 'sysdtls' as 'sysdtl'
        dtl = sysdtl.readlines() # > list every detail according to it's line
    print(dtl[4]) # > prints line 4 from main.txt (system's build number)
