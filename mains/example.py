from models.model import Model
from keras.models import Sequential

# main section where the execution begins

seq = Sequential()

model = Model(seq)

model.build()
model.train()
model.save()


