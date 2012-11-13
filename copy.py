#Filename: copy.py
#Author: bonnshore

import os
import mkdir
import glob
import star_ops

class Copy:
    def __init__(self,old,new):
	self.old = old
	self.new = new
	return

    def copydirs(self,sourceDir,targetDir):
	targetDir = targetDir + os.path.split(sourceDir[:-1])[1]
	for f in os.listdir(sourceDir):
	    sourceF = os.path.join(sourceDir, f) 
	    targetF = os.path.join(targetDir, f)
	    if os.path.isfile(sourceF):
		if not os.path.exists(targetDir):
		     os.makedirs(targetDir)
		if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
		    open(targetF, "wb").write(open(sourceF, "rb").read())
		else:
		    print '%s EXISTS Already!' % (sourceF)
	    elif os.path.isdir(sourceF):
		self.copydirs(sourceF,targetF)
	    else:
		pass
	return 
	    
    def copyfile(self,old):
	sourceF = old
	targetF = self.new + os.path.split(old)[1]
	if not os.path.exists(targetF) or (os.path.exists(targetF) and (os.path.getsize(targetF) != os.path.getsize(sourceF))):
	    open(targetF, "wb").write(open(sourceF, "rb").read())
	else:
	    print '%s EXISTS Already!' % (sourceF)
	return

    def real_copy(self,old,new):
	if os.path.isdir(old):
	    self.copydirs(old,new)
	elif os.path.isfile(old):
	    self.copyfile(old)
	else:
	    pass
	return

    def is_destination_exists(self,old,new):
	if not os.path.exists(new):
	    print 'The destination not exists, we will Create the shit!'
	    mkd = mkdir.Mkdir(new)
	    mkd.make_dir()
	self.real_copy(old,new)
	return
	
    def copy_func(self): 
	if not os.path.exists(self.old):
	    if star_ops.is_star_cmd(self.old):
		cp_list = glob.glob(self.old)
		for item in cp_list:
		    self.is_destination_exists(item,self.new)
	    else:
		print 'Target NOT EXISTS!'
	else:
	    self.is_destination_exists(self.old,self.new)
	return
