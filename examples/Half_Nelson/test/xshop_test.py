import os
import subprocess

def run(run_function):
    run_function('target','run_exploit')

def run_exploit():
    subprocess.call(['gcc','half-nelson.c','-lrt'])
    p = subprocess.Popen(['./a.out'],stdout=subprocess.PIPE)
    output = p.stdout.read()
    print output
    if "Got root!" in output:
        return 2
    else:
        return 0
    