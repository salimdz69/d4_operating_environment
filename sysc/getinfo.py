# needed to access file
import os

# Importing system details :
sysdtls = os.path.join('syscnf', 'sysdtl', 'main.txt')

with open(sysdtls, 'r') as sysdtl:  # > opens 'sysdtls' as 'sysdtl'
    dtl = sysdtl.readlines()  # > list every detail according to it's line


def get_info(line):

    return dtl[line]
