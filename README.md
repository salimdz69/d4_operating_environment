| 'd4' Operating environment |

# Introduction / Overview
# Features / Core concepts
# Limitations / Problems
# Future plans
# How to start (setup, run, use)
# Core structure (filesystem, commands)

- Introduction / Overview :

> what is "'d4' Operating environment"?
× "directory 4 Operating environment" (or "d4 OE" for short) is an open-source project released under the MIT license to simulate a mini-os like environment while being totally free to use and modify by small developers.

> what's the purpose of this project?
× the purpose of this project is to simulate a mini-os like environment that can be modified and contributed-in by small developers.

> what's the state of this project so far?
× 'd4oe' is in a prototype state, so it's still under heavy development, expect huge changes in future updates and patches.

> how can i be a part of this?
× you can contribute in this project by various ways like :
. giving feedback and suggestions while testing this project
. doing pull requests and changes to the porject's source code
. adding your own applications and code to it's source code
. forking and making your own projects based on this project's code

- Features / Core concepts :
> Basic filesystem
> Multi-modules importing
> Built-in commands

- Limitations / Problems :
> Core features under development
> Slow development (author has life)
> Author still don't know how git works

- Future plans :
> More advanced filesystem
> filesystem interactions (read, write, create, delete)
> users and filesystem permissions
> Error handling

- How to start (setup, run, use) :

1. clone the project's repository :

git clone https://github.com/salimdz69/d4_operating_environment

2. go to the project's directory :

cd d4_operating_environment

3. run the project :

python3 run.py

- Core structure (filesystem, commands) :
> Filesystem :
. sysc : where all the system's commands live (sysinfo, sysext, ...)
. sysap : where all the system's applications are located (app.py, something.py, ...) [NOTE : application-related features are stll under development and not implemented]
. syscnf : a place for all configurations (sysdtl, syscl, ...) [NOTE : configuration-related features are stll under development and implemention]
. sysusr : the user space for his work [NOTE : user-related features are stll under development and not implemented]

> Commands (built-in) :
. sysinfo : displays information about d4
. sysver  : shows version of d4
. sysvcn  : shows version code name of d4
. sysbldn : shows build number of d4
. sysrlsd : shows release date of d4
. sysext  : stops d4

Copyright (c) 2025 SalimDZ