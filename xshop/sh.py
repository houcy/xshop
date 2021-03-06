"""
sh module

Allows running of shell commands, with proper logging.
"""

import logging
import subprocess

def run(command, shell=False):
    """
    Run the specified command and log the results.
    """
    process = subprocess.Popen(command, 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=shell)

    output = ""
    while process.poll() is None:
        line=process.stdout.readline()
        logging.debug(line)
        output+=line

    stdout,stderr = process.communicate()
    logging.debug(stdout)
    
    stdout = output+stdout
    logging.error(stderr)
    
    return {'return_code':process.returncode,'stdout':stdout,'stderr':stderr}
