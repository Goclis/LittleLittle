#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import shutil


# Remove directories and files
# 删除rootdir下的名字在dirs_to_delete中的文件夹
# 删除rootdir下名字为files_to_delete中的文件
def rmdfs(rootdir, dirs_to_delete, files_to_delete = []):
	for (dirpath, subdirs, filenames) in os.walk(rootdir):
		for f in filenames:
			if f in files_to_delete:
				path = os.path.join(dirpath, f)
				os.remove(path)
				print 'File %s deleted.' % path

		for subdir in subdirs:
			if subdir in dirs_to_delete:
				path = os.path.join(dirpath, subdir)
				shutil.rmtree(path)
				print 'Directory %s deleted.' % path

		subdirs[:] = [d for d in subdirs if d not in dirs_to_delete]


def main():
	cwd = os.getcwd()
	dirs = ['Debug', 'Release', 'ipch']
	files = ['zrddsgen.sdf']
	try:
		rmdfs(cwd, dirs, files)
	except:
		print u'Error: Please try again after closing the Visual Studio.'

	os.system("pause")


if __name__ == '__main__':
	main()
