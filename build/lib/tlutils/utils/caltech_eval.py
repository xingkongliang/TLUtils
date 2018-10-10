#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

def run_matlab_eval_code(matlab_code_dir, version, branch='0', iter_now='12999'):
    """
    matlab_code_dir = '/media/tianliang/Projects/Caffe2_Projects/detectron-data/pedestrian_datasets'
    version = 'v9_09'
    branch = '1'  # if true for eval all
    iter_now = '12999'  
    """

    comand = 'cd {} && matlab -nodesktop -nodisplay -nojvm -nosplash -r "dbEval_Faster {} {} {};quit"'.format(
        matlab_code_dir, version, branch, iter_now)

    f = os.popen(comand)
    data = f.readlines()
    f.close()

    f2 = open("results_{}.txt".format(version), 'w')
    f2.writelines(data)
    f2.close()

    os.system('cat "results_{}.txt"'.format(version))

    return True

