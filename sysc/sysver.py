# | 'sysver' |
# 'sysver' is a built-in command for the 'd4' operating environment to show the system version of 'd4'.
# 'sysver' comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysver' is in a stable development state, but expect changes in further updates.

# Importing required libraries :
import getinfo # > used to import system details


# Main functionality :
def main():
    print(getinfo.get_info(2))
