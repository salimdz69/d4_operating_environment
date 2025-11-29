# | 'sysinfo' |
# 'sysinfo' is a built-in command for the 'd4' operating environment project to show information about 'd4'.
# 'sysinfo' comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# 'sysifo' is in a stable development state, but expect changes in further updates.

import getinfo


# Main functionality :
def main():
    print("- Description  :", getinfo.get_info(1)) # > prints line 1 from main.txt (system's description)
    print("- Version      :", getinfo.get_info(2)) # > prints line 2 from main.txt (system's version)
    print("- Code name    :", getinfo.get_info(3)) # > prints line 3 from main.txt (system's version code name)
    print("- Build number :", getinfo.get_info(4)) # > prints line 4 from main.txt (system's build number)
    print("- Release date :", getinfo.get_info(5)) # > prints line 5 from main.txt (system's release date)
