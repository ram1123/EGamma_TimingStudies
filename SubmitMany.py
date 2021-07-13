# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-13
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-13

import os

from GetConfig import ListOfPaths

# print ListOfPaths


for count, paths_ in enumerate(ListOfPaths):
    print("===")
    command1 = "python3 /data/timing/scripts/timing/submit.py hlt_config_13July_%s.py"%(str(count))
    command2 = "python3 /data/timing/scripts/timing/submit.py hlt_config_13July_Sum_%s.py"%(str(count))
    print("Command: {}".format(command1))
    os.system(command1)
    print("Command: {}".format(command2))
    os.system(command2)