# | 'run' |
# this is 'run', the thing that runs 'd4oe', it manages commands, applications and configurations, and works as a temporary shell untill 'protoshell' is ready to be used.
# this... script? or whatever is it comes under d4's MIT license and it's totally free to use and modify, use it and it's source code wisely.
# this script is not in a stable development state, so expect changes in further updates.

# # Importing required libraries :
import sys # > used to import system commands, applications and configurations

# importing system directories :
# > sysc (for commands) :
sys.path.append('sysc')
# import command > imports 'command' from 'command.py'
import sysinfo
import sysver
import sysvcn
import sysbldn
import sysrlsd
import sysext
# > sysap (for applications) :
sys.path.append('sysap')
# import app > imports 'app' from 'app.py' or 'app/main.py' or smth idk lol
import syswlcm
# > syscnf (for configurations) :
sys.path.append('syscnf')
# still working on this thing :)

syswlcm.main()
while True: # > Main loop :
    usrin = input("> ") # > user input (the way to type commands)
#   if userin == 'command':
#       command.main() > do that command
    if usrin == 'sysinfo':
        sysinfo.main()
    elif usrin == 'sysver':
        sysver.main()
    elif usrin == 'sysvcn':
        sysvcn.main()
    elif usrin == 'sysbldn':
        sysbldn.main()
    elif usrin == 'sysrlsd':
        sysrlsd.main()
    elif usrin == 'sysext':
        sysext.main()
    else:
        print("***", f"'{usrin}'" + " IS AN INVALID COMMAND ***") # > used when you type a non-existent command
