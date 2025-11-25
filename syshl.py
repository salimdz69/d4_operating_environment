# | 'protoshell' ver 0.1 |
# 'protoshell' is a simple and a temporary shell that was made for the 'd4' operating environment project for test purposes (and as a placeholder).
# 'protoshell' comes with no license and it's totally free to use and modify, use it and it's source code wisely. 
# 'protoshell' is still under heavy development (unstable), expect huge changes in-fuctionality and in-code next version

# Imports main commands 
import syswlcm
import syscrdt
import sysinfo
import sysver
import syscn
import sysbldn
import sysrlsd
import sysco
import sysexit

# Main variables :
# > this one is for the main loop
main = True
# > this one is for user input
usrin = 0
# > shell info (shell name, shell version)
shlnam = "protoshell"
shlver = "0.1"

# Main functions :
# > shlinfo : made to show info about the shell
def shlinfo():
    print("- Shell name    :", shlnam)
    print("- Shell version :", shlver)
# > main : a loop for the actual shell stuff (the way to type commands)
syswlcm.main()
shlinfo()
while main:
    usrin = input("> ")
    if usrin == "":
        print()
    elif usrin == "syscrdt":
        syscrdt.main()
    elif usrin == "sysinfo":
        sysinfo.main()
    elif usrin == "sysver":
        sysver.main()
    elif usrin == "syscn":
        syscn.main()
    elif usrin == "sysbldn":
        sysbldn.main()
    elif usrin == "sysrlsd":
        sysrlsd.main()
    elif usrin == "sysco":
        sysco.main()
    elif usrin == "sysexit":
        sysexit.main()
    else:
        print("***", f"'{usrin}'" + " IS AN INVALID COMMAND/TASK ***")
