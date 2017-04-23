import pickle
import numpy as np
from scipy import misc
import glob
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Convolution2D, MaxPooling2D
from keras.optimizers import SGD

positions = pickle.load( open( "positions.p", "rb" ))

image_paths = glob.glob("blenderpics/*.png")

images = np.array([misc.imread(image_path) for image_path in image_paths])
print(images.shape)
print(np.array(positions).shape)


model = Sequential()
# input: 100x100 images with 3 channels -> (3, 100, 100) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(128, 128, 3), dim_ordering="tf"))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3, dim_ordering="tf"))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='valid'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
# Note: Keras does automatic shape inference.
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(1))
#model.add(Activation('softmax'))

sgd = SGD(lr=1e-8, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mean_squared_error', optimizer=sgd)
while True:
    model.fit(images[:-10], positions[:-10], batch_size=32, nb_epoch=1)

    print(model.predict(images[-10:]))
    print(positions[-10:])
