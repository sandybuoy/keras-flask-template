# do not modify this file
# Run this file to deploy the chosen model version

from shutil import copy2
from os.path import exists
from utils import path, config
i = int(input('Enter the model version to be deployed: '))
src = path() + '/Experiments/' + config()['NAME'] + '/' + config()['NAME'] + '_model_v'+str(i)+'.h5'
dst = path() + '/deploy_model/model.h5'
if exists(src):
    copy2(src, dst)
else:
    print('Enter a valid input!')
