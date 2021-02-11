# git-copy-all
#	copy a git repository and all its branches
#
# created by Jonathan Markovsky, jon.markov@icloud.com, 2021/02/10
#

import subprocess

try:
	cpr = subprocess.run(
		['echo',
		'hello world'], 
		capture_output=True, 
		text=True,
		check=True)
	print(cpr.stdout)

	cpr = subprocess.run(
		['git','fetch','origin'], 
		capture_output=True, 
		text=True, 
		check=True)
	print(cpr.stdout)

	cpr = subprocess.run(
		['git','branch','-a'], 
		capture_output=True, 
		text=True, 
		check=True)
	lines = cpr.stdout.split('\n')
	print(repr(lines))
	head = lines[0]
	[am, mainbranch] = head.split()
	print("mainbranch = " + mainbranch)
	for line in lines[2:] :
		branchparts = line.split('/')
		if len(branchparts) >= 3 :
			if not mainbranch in branchparts[2] :  
				print(branchparts[2])

				cpr = subprocess.run(
					['git','checkout','-b',branchparts[2],'origin/' + branchparts[2]], 
					capture_output=True, 
					text=True, 
					check=True)
				print(cpr.stdout)





except subprocess.CalledProcessError as ec:
	print("CalledProcessError occurred! cmd=\'", ec.cmd, "\'")
	print(ec.stderr)
	print("   ...exiting.")
	exit()



