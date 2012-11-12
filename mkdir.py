#Filename: mkdir.py
#Author: bonnshore

import os

class Mkdir:
    def __init__(self,target_dir):
	self.dir = target_dir
	return

    def make_dir(self):
	if not os.path.exists(self.dir):
	    os.makedirs(self.dir)
	else:
	    print 'Dir EXISTS Already!'
	return
