#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import os.path
import shutil


# 删除rootdir下的名字在dirs_to_delete中的文件夹
def rmdir(rootdir, dirs_to_delete):
	for (dirpath, subdirs, filenames) in os.walk(rootdir):
		for subdir in subdirs:
			if subdir in dirs_to_delete:
				print 'Delete dir %s' % os.path.join(dirpath, subdir)
				shutil.rmtree(os.path.join(dirpath, subdir))

		subdirs[:] = [d for d in subdirs if d not in dirs_to_delete]


def main():
	cwd = os.getcwd()
	dirs = ['Debug', 'Release', 'ipch']
	rmdir(cwd, dirs)


if __name__ == '__main__':
	main()