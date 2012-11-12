# Filename: cmdMain.py
# Author: bonnshore

import sys
import os
import dirlist
import remove
import mkdir
import move
import string
import copy
import rename
import help_txt

if __name__ == "__main__":

    print 'This is bonn Stupid File Managment!\n'\
	'Input some cmds to run basic operation for File and Directory!\n'\
	'Such as CURD and Backup.\n'\
	"input '--help' for help.\n"\
	'Enjoy it!\n'

    argv = [] #command arguments list
    while True: #endless loop untill exit
	argv = string.split(raw_input('$==>'))
	while len(argv) != 0: #User input nothing
	    if argv[0] == 'quit': #Quit
		print 'See you!'
		exit()
	    elif argv[0] == 'ls': #list dir
		if len(argv) <= 1:
		    dlist = dirlist.Dirlist()
		    dlist.get_current_list()
		elif len(argv) == 2:
		    dlist = dirlist.Dirlist()
		    dlist.get_path_list(argv[1])
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'rm': #remove
		if len(argv) <= 1:
		    print 'Miss target to REMOVE!'
		elif len(argv) == 2:
		    rm = remove.Remove(argv[1])
		    rm.is_that_exists() 
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'mkdir': #create new directory
		if len(argv) <= 1:
		    print 'Miss target dir to CREATE!'
		elif len(argv) == 2:
		    makedir = mkdir.Mkdir(argv[1])
		    makedir.make_dir()
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'mv': #move
		if len(argv) <= 1:
		    print 'Miss target to MOVE!'
		elif len(argv) == 2:
		    print 'Miss destination to MOVE!'
		elif len(argv) == 3:
		    mv = move.Move(argv[1],argv[2])
		    mv.move_dir()
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'cp': #copy
		if len(argv) <= 1:
		    print 'Miss target to COPY!'
		elif len(argv) == 2:
		    print 'Miss destination to COPY'
		elif len(argv) == 3:
		    cp = copy.Copy(argv[1],argv[2])
		    cp.copy_func()
		else:
		    print 'REDUNDANT arguments!'	
	    elif argv[0] == 'rn': #rename
		if len(argv) <= 1:
		    print 'Miss target to rename!'
		elif len(argv) == 2:
		    print 'Miss the new filename'
		elif len(argv) == 3:
		    rn = rename.Rename(argv[1],argv[2])
		    rn.re_name()
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'bk': #backup
		bak_cmd = 'python backup.py'
		os.system(bak_cmd)
	    elif argv[0] == 'vim': #open vim to edit file
		if len(argv) == 1:
		    os.system('gvim')
		elif len(argv) == 2:
		    os.system('gvim ' + argv[1])
		else:
		    print 'REDUNDANT arguments!'
	    elif argv[0] == 'whoami' and len(argv) == 1: #who are you
		print 'Stupid User in Stupid Software\non Python '\
			+ string.join(string.split(sys.version)[0:6])
	    elif argv[0] == '--help' and len(argv) == 1: #help info
		help_txt.print_help()  
	    else:
		print 'WRONG commands!' #Wrong Commands inputed
	    argv = []
	else:
	    pass
    else:
	pass
