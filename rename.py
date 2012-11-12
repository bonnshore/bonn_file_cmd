#Filename: rename.py
#Author: bonnshore

import os

class Rename:
    def __init__(self,old,new):
	self.old = old
	self.new = new
	return
    
    def re_name(self):
	if not os.path.exists(self.old):
	    print 'the file you want to rename is NOT exists!'
	else:
	    os.rename(self.old,self.new)
	return
