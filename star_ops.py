#Filename: star_ops.py
#Author: bonnshore

import re
import os
import glob
import copy

def is_star_cmd(args):
    argv = os.path.split(args)[1]
    reg = '^\*'
    pattern = re.compile(reg)
    match = pattern.search(argv)
    return match

def star_rm(args):
    rm_list = glob.glob(args)
    for item in rm_list:
	os.remove(item)
    return
