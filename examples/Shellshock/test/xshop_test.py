from subprocess import call
import os
def run(H):
	H.run('target','run_exploit')

def run_exploit():
	cve = os.environ['cve'] 
	if call(['./'+cve+'.sh']):
		return 2
	else:
		return 0
