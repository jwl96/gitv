import sys
from commands import getstatusoutput as gso


def run(file_pattern, grep_pattern):
	file_list = gso('git ls-files ' + gso('git rev-parse --show-toplevel')[1])[1].split('\n')
	
	for file_name in file_list :
		if file_pattern in file_name :
			with open(file_name, 'r') as f :
				c = f.read()
			
			i = 1
			for line in c.split('\n') :
				if grep_pattern in line :
					print file_name + ':' + str(i) + ':' + line.strip()
				i += 1
	


if len(sys.argv) != 4 :
	print 'Invalid Arguments\nUsage: gitv.py findgrep <file_pattern> <grep_pattern>'

else :
	if sys.argv[1] != 'findgrep' :
		print 'Unsupported Command'
	else :
		run(sys.argv[2], sys.argv[3])

