import sys
from utils.utils import path, config, getVersion
from os import chmod
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
from glob import glob


class Log:
    def __init__(self):   # do not modify this section
        # for fetching the experiment folder in the Experiment folder directory
        parent_path = path() + '/Experiments/' + config()['NAME'] + '/' + config()['NAME']
        files = glob(parent_path + '*.txt')

        # changing the file permission to read/write mode
        for i in files:
            chmod(i, S_IWUSR | S_IREAD)

        # creating the log file
        self.logs = open(parent_path + '_logs_v' + str(getVersion()) + '.txt', 'w')
        # transferring the console output to log file
        sys.stdout = self.logs

    def save(self):  # do not modify this section
        parent_path = path() + '/Experiments/' + config()['NAME'] + '/' + config()['NAME']
        # closing the log file
        self.logs.close()

        # splitting the log file
        logs = open(parent_path + '_logs_v' + str(getVersion()-1) + '.txt')
        data = logs.read()
        logs.close()
        data = data.split('-----------------------------------------------------------------')

        # writing parameters specific data
        f = open(parent_path + '_parameters_v' + str(getVersion()-1) + '.txt', 'w')
        f.write(data[0])
        f.close()

        # writing performance specific data
        f = open(parent_path + '_performance_v' + str(getVersion()-1) + '.txt', 'w')
        f.write(data[1])
        f.close()

        # changing file permission to read only mode
        files = glob(parent_path + '*.txt')
        for i in files:
            chmod(i, S_IREAD | S_IRGRP | S_IROTH)


