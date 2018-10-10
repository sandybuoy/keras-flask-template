from os.path import dirname, abspath, exists, getctime
from os import makedirs
import json
from glob import iglob, glob
import re


def path():  # do not modify this section
    return dirname(dirname(abspath(__file__)))  # returns the root directory of the template


def config():  # do not modify this section
    with open(path() + '/config/file.json') as f:
        data = json.load(f)
    return data  # fetches the data from the json and returns in the form of a dictionary


def params():  # do not modify the section
    data = config()
    print("{:<30} {:<10}".format('Model Specific Parameters', 'Value'))
    print('_________________________________________________________________')
    for label, num in data.items():
        print("{:<30} {:<10}".format(label, num))  # write the model specific parameters into the log file


def save(model):  # do not modify this section
    print('\nSaving Model...')
    # apply save login here
    parent_path = path() + '/Experiments/' + config()['NAME'] + '/' + config()['NAME']
    name = parent_path + '_model_v'+str(getVersion())+'.h5'
    model.save(name)

    print('Model is successfully saved to the disk')
    print('_________________________________________________________________')


def make_dir():  # do not modify this section
    new_dir = path()+'/Experiments/'+config()['NAME']
    if not exists(new_dir):
        makedirs(new_dir)  # creates Experiments directory


def summarize(summary):  # do not modify this section
    filepath = path() + '/Experiments/' + config()['NAME'] + '/summary.csv'
    if not exists(filepath):
        f = open(filepath, 'w')
        f.write('Version,Epochs,Hidden Layers,Dropout,Optimizer,Loss Function,Validation Loss,Validation Accuracy,Loss,Accuracy')
        f.close()
    # writes the summary into the csv file
    write = str(getVersion()-1)+','+str(config()['NB_EPOCH'])+','+str(config()['N_HIDDEN'])+','+str(config()['DROPOUT'])+','+config()['OPTIMIZER']+','+config()['LOSS']+','
    for i in summary.values():
        write += str((i[-1])) + ','
    write = write[:-1]
    f = open(filepath, 'a')
    f.write('\n')
    f.write(write)
    f.close()


def getVersion():  # do not modify this section
    # this section generates the new model version every time
    modelpath = path() + '/Experiments/' + config()['NAME'] + '/' + config()['NAME'] + '_model_v*.h5'
    if glob(modelpath):
        newest = max(iglob(modelpath), key=getctime)
        m = re.search('v(.+?).h5', newest)
        if m:
            return int(m.group(1))+1
    return 0
