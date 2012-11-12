#Filename: dirlist.py
#Author: bonnshore

import os
import string

class Dirlist:
    def __init__(self):
	return

    def get_current_list(self):
	current_path = os.getcwd()
	print string.join(os.listdir(current_path)).replace(' ','  ')
	return

    def get_path_list(self,arg):
        print string.join(os.listdir(arg)).replace(' ','  ')
	return
