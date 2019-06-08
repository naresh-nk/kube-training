#!/usr/bin/env python

import os
import subprocess
import sys

return_result = ''
error_message = ''
return_code = 0

command = sys.argv[1]

def run_command(command):
  command = command
  try:
    response = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    output,error = response.communicate()

    if output:
      return_result = output
      return_code = response.returncode

    if error:
      return_code = response.returncode
      error_message = error.strip()

  except Expection as e:
    return_code = 1
    error_message = e

if __name__ =='__main__':
  result = run_command(command)
  print(return_result, return_code, error_message)
