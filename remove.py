#Filename: remove.py
#Author: bonnshore

import os
import star_ops

class Remove:
    def __init__(self,args):
	self.args = args
	return

    def recursion_rm(self,dirpath):
	for item in os.listdir(dirpath):
	    tempath = os.path.join(dirpath,item)
	    if os.path.isfile(tempath):
		os.remove(tempath)
	    elif os.path.isdir(tempath):
		self.recursion_rm(tempath)
	    else:
		print 'Remove ERROR!'
	os.rmdir(dirpath)
	return
		
    def rm_the_shit(self):
	if os.path.isfile(self.args):
	    os.remove(self.args)
	else:
	    dirpath = self.args
	    self.recursion_rm(dirpath)
    
    def is_that_exists(self):
	if not os.path.exists(self.args):
	    if star_ops.is_star_cmd(self.args):
		star_ops.star_rm(self.args)
	    else:
		print 'WRONG path!'
	else:
	    self.rm_the_shit()
