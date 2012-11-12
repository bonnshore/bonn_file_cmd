#Filename: backup.py
#Author: bonnshore
import os
import fnmatch
import mkdir
import glob
import time


class Backup:
    dirlist = []

    def __init__(self):
	return

    def get_target_dir(self):
	target_dir = raw_input('Enter the dir you want to backup to:')
	if not os.path.exists(target_dir):
	    print 'The path you input is NOT exists!\nwe will create the shit!'
	    mk = mkdir.Mkdir(target_dir)
	    mk.make_dir()
	return target_dir
    
    def star_file(self,path_to_backup):
	file_list = glob.glob(path_to_backup)
	for item in file_list:
	    Backup.dirlist.append(item)
	return

    def Is_a_file(self): 
	path_to_backup = raw_input('Enter the file path you want to backup:')
	if fnmatch.fnmatch(path_to_backup,'*'):
	    self.star_file(path_to_backup)
	else:
	    while not(os.path.exists(path_to_backup)):
		print 'File Path WRONG!'
		path_to_backup = raw_input('Enter the file path you want to backup:')
	    else:
		Backup.dirlist.append(path_to_backup)
	return
    
    def Is_a_dir(self):
	path_to_backup = raw_input('Enter the dir you want to backup:')
	while not(os.path.exists(path_to_backup)):
	    print 'dir path WRONG!'
	    path_to_backup = raw_input('Enter the dir you want to backup:')
	else:
	    bk_list = os.listdir(path_to_backup)
	    for item in bk_list:
		item = path_to_backup + item
		Backup.dirlist.append(item)
	return

    def run_backup(self, target_dir):
	today = target_dir + time.strftime('%Y%m%d')
	now = time.strftime('%H%M%S')
	comment = raw_input('Enter your comment:')
	if len(comment) == 0:
	    target = today + os.sep + now + '.zip'
	else:
	    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
	if not os.path.exists(today):
	    os.mkdir(today)
	    print 'Create ' + today + ' successfully!'
	zip_cmd = "zip -qr %s %s" % (target,' '.join(Backup.dirlist))
	if os.system(zip_cmd) == 0:
	    print 'BACKUP SUCCESSFULLY TO', target
	else:
	    print 'BACKUP FAILED!'
	return

if __name__ == "__main__":
    command = raw_input('IF you want to backup one file input f.\n'
	    'IF you have a directory to backup input d.\n'
	    'Nothing to do input OTHER key.\n'
	    '$--backup-->')
    back = Backup()
    if command == 'f':
	back.Is_a_file()
	back.run_backup(back.get_target_dir())
    elif command == 'd':
	back.Is_a_dir()
	back.run_backup(back.get_target_dir())
    else:
	exit()
