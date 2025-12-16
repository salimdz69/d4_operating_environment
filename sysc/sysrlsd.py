# | 'sysrlsd' |
# 'sysrlsd' is a built-in command for the 'd4' operating environment to show the system release date of 'd4'.
# 'sysrlsd' comes under d4's MIT licnese and it's totally free to use and modify, use it and it's source code wisely.
# 'sysrlsd' is in a stable development state, but expect changes in further updates.

# Importing required libraries :
import getinfo # > used to import system details


# Main functionality :
def main():
    print(getinfo.get_info(5))

