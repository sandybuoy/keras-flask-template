from split_process.split_process import SplitProcess
from keras import layers
from keras.optimizers import *
from utils.utils import config, params, save, make_dir, summarize
from logger.logs import Log
import timeit


class Model:

    def __init__(self, model):  # do not modify this section
        self.config = config()  # fetches the configuration from the json file
        make_dir()  # creates the Experiment directory
        self.logs = Log()  # creates the log file
        self.summary = None  # initializes summary variable
        params()  # pushes parameters values into log file
        self.model = model  # initialize the model passed
        self.data = SplitProcess()  # creates object of SplitProcess class
        self.data.split()  # splits the data
        self.data.process_data()  # process the data

    def build(self):  # do not alter any print statements here
        print('Deep Learning Model Architecture...')

        # Network Architecture
        # start modification
        self.model.add(layers.Conv2D(32, (3, 3), activation='relu',
                                     input_shape=(150, 150, 3)))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(64, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Conv2D(128, (3, 3), activation='relu'))
        self.model.add(layers.MaxPooling2D((2, 2)))
        self.model.add(layers.Flatten())
        self.model.add(layers.Dense(512, activation='relu'))
        self.model.add(layers.Dense(1, activation='sigmoid'))
        self.model.summary()
        # end modification
        print('-----------------------------------------------------------------', end='')
        print('Compiling the model with ')
        start = timeit.default_timer()

        # Compiling the model
        # start modification

        print('Loss: ' + self.config['LOSS'])
        print('Optimizer: ' + self.config['OPTIMIZER'])
        print('Metrics: ' + self.config['METRICS'])
        self.model.compile(loss=self.config['LOSS'],
                           optimizer=eval(self.config['OPTIMIZER']),
                           metrics=[self.config['METRICS']])
        # end modification
        stop = timeit.default_timer()
        print('Finished Compiling in ' + str(stop - start) + 's')
        print('_________________________________________________________________')

    def train(self):  # do not alter any print statements here
        print('\nStarted Training...')
        start = timeit.default_timer()

        # start modification
        self.summary = self.model.fit_generator(
            self.data.X_train,
            verbose=self.config['VERBOSE'],
            steps_per_epoch=self.config['STEPS_PER_EPOCH'],
            epochs=self.config['NB_EPOCH'],
            validation_data=self.data.X_test,
            validation_steps=self.config['VALIDATION_STEPS'])

        # end modification

        stop = timeit.default_timer()
        print('Completed Model Training in ' + str(stop - start) + 's')
        print('_________________________________________________________________')

    def save(self):  # do not modify this section
        save(self.model)
        summarize(self.summary.history)
        self.logs.save()
