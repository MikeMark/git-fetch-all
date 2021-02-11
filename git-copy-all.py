# git-copy-all
#	copy a git repository and all its branches
#
# created by Jonathan Markovsky, jon.markov@icloud.com, 2021/02/10
#

import subprocess

cpr = subprocess.run(['echo','hello world'], capture_output=True, text=True)
print(cpr.stdout)
