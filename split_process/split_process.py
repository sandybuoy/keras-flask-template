from utils.utils import config, path
from keras.preprocessing.image import ImageDataGenerator


class SplitProcess:

    def __init__(self):
        self.X = None
        self.y = None
        self.X_train, self.X_test, self.y_train, self.y_test = None, None, None, None
        self.config = config()  # fetches the configuration from the json file

    def split(self):
        # fetch the data
        #######################
        # Do splitting here!
        # start modification
        #######################
        # end modification
        pass

    def process_data(self):
        validation_dir = path() + '/data/validation'
        train_dir = path() + '/data/train'

        # do the reshaping
        # start modification
        #######################
        # end modification

        # normalize the data
        # start modification
        train_datagen = ImageDataGenerator(rescale=1. / 255)
        validation_datagen = ImageDataGenerator(rescale=1. / 255)
        # end modification

        # loading the training data
        self.X_train = train_datagen.flow_from_directory(
            train_dir,
            target_size=(150, 150),
            batch_size=config()['BATCH_SIZE'],
            class_mode='binary')

        # loading the validation data
        self.X_test = validation_datagen.flow_from_directory(
            validation_dir,
            target_size=(150, 150),
            batch_size=config()['BATCH_SIZE'],
            class_mode='binary')
