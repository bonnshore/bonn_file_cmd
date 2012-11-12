#Filename: move.py
#Author: bonnshore

import shutil 
import os
import mkdir
import remove
import star_ops
import glob

class Move:
    def __init__(self,old,new):
	self.new = new
	self.old = old
	return

    def real_move(self,old):
	try:
	    shutil.move(old,self.new)
	except shutil.Error:
	    cmd = raw_input('The target you move in destination already EXISTS!\n'
		    'input y to COVER other key to GIVEUP.\n')
	    if cmd == 'y':
		rm = remove.Remove(self.new + old)
		rm.rm_the_shit()
		shutil.move(old,self.new)
	    else:
		pass
	return

    def move_dir(self): 
	if not os.path.exists(self.old):
	    if star_ops.is_star_cmd(self.old):
		mv_list = glob.glob(self.old)
		for item in mv_list:
		    self.real_move(item)
	    else:
		print 'Target NOT EXISTS!'
	else:
	    if os.path.exists(self.new):
		self.real_move(self.old)	
	    else:
		print 'The destination not exists, I will Create the shit!'
		mkd = mkdir.Mkdir(self.new)
		mkd.make_dir()
		self.real_move(self.old)	
	return
