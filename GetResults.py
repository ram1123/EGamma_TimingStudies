# -*- coding: utf-8 -*-
# @Author: Ram Krishna Sharma
# @Author Email: ram.krishna.sharma@cern.ch
# @Date:   2021-07-14
# @Last Modified by:   Ram Krishna Sharma
# @Last Modified time: 2021-07-15
import os

pathToCheck = "/data/timing/output/rasharma/"
# dirToCheck = "CMSSW_11_3_0.20210713"
dirToCheck = "CMSSW_12_1_0.20211126"

# /data/timing/jobs/rasharma/CMSSW_12_1_0.20211126_004703

# AllDirs = os.listdir(pathToCheck)

# for dir_ in AllDirs:
#     if dirToCheck in dir_:
#         print("Directory: {}".format(dir_))

command = 'cat '
for dirpath, dirnames, files in os.walk(pathToCheck):
    if dirToCheck in dirpath:
        # print("=================")
        # print('Found directory: {}'.format(dirpath))
        for files_ in files:
            if files_.endswith('.csv'):
                num_lines = sum(1 for line in open(os.path.join(dirpath, files_)))
                if num_lines == 4:
                    # print(files_)
                    # os.system('cat '+os.path.join(dirpath,files_))
                    command = command + " " + os.path.join(dirpath, files_)

os.system(command + " > Individual_Path_timings.csv")

command = 'cat '
dict_files = {}
for dirpath, dirnames, files in os.walk(pathToCheck):
    if dirToCheck in dirpath:
        # print("=================")
        # print('Found directory: {}'.format(dirpath))
        for files_ in files:
            if files_.endswith('.csv'):
                num_lines = sum(1 for line in open(os.path.join(dirpath, files_)))
                # if num_lines == 4:
                #     for line in open(os.path.join(dirpath, files_)):
                #         if ""
                if num_lines != 4:
                    # print(files_)
                    dict_files[num_lines] = os.path.join(dirpath, files_)
                    # os.system('cat '+os.path.join(dirpath,files_))
                    command = command + " " + os.path.join(dirpath, files_)

os.system(command + " > Many_PathTogether_timings.csv")

command = 'cat '
for num, files in dict_files.items():
    print(num, files)
    command = command + " " + files

os.system(command + " > Many_PathTogether_timings_ordered.csv")
