import os
fname = "machine+learning.txt"
fp = open(fname, 'r')

readline = fp.readline()

while(readline):
	print("Processing", readline) 
	syscall = "git clone " + readline
	os.system(syscall)
	readline = fp.readline()


