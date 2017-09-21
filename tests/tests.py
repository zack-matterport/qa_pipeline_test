# tests.py

import random
import time
import subprocess
from subprocess import Popen, PIPE

try:
    import unittest2 as unittest
except ImportError:
    import unittest




# call the testcases
class ProTests(unittest.TestCase):

    def test_Pro10sweeps(self):
      try:
        print ("process image")
        cmd = "cd /mnt/dev/mp_vision-build/deploy/ && ./vision_mesh_code.work /mnt/dev/mp_vision-build/deploy/ /mnt/dev/testResults/emptymesh/"
        process = subprocess.check_call(cmd, shell=True)


        print ("test image")
        cmd = "cd /mnt/dev/qa/automation/jenkins/ && ./imageCompare.sh '/mnt/dev' .1 'pan/high' '72e2e8bdf87c45e29d023e7e18af1cc1_skybox1.jpg' '01sweep'"
        process = subprocess.check_call(cmd, shell=True)

      except:
        return False

      return True




if __name__ == '__main__':
    unittest.main()