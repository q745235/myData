from tensorflow import keras
import tensorflow
import os, shutil
from tensorflow.keras import layers
from tensorflow.keras import models
from tensorflow.keras import optimizers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.layers import BatchNormalization

# image classification

# The path to the directory where the original
# dataset was uncompressed
print('1')
original_dataset_dir = 'C:/Users/user/DL/00/data/train'

# The directory where we will
# store our smaller dataset
base_dir = 'falldown/data/fall_and_notfall'
# os.mkdir(base_dir)

# Directories for our training,
# validation and test splits
train_dir = os.path.join(base_dir, 'train')
# os.mkdir(train_dir)
validation_dir = os.path.join(base_dir, 'validation')
# os.mkdir(validation_dir)
test_dir = os.path.join(base_dir, 'test')
# os.mkdir(test_dir)
print('2')
# Directory with our training fall pictures
train_fall_dir = os.path.join(train_dir, 'fall')
# os.mkdir(train_fall_dir)

# Directory with our training notfall pictures
train_notfall_dir = os.path.join(train_dir, 'notfall')
# os.mkdir(train_notfall_dir)

# Directory with our validation fall pictures
validation_fall_dir = os.path.join(validation_dir, 'fall')
# os.mkdir(validation_fall_dir)

# Directory with our validation notfall pictures
validation_notfall_dir = os.path.join(validation_dir, 'notfall')
# os.mkdir(validation_notfall_dir)

# Directory with our validation fall pictures
test_fall_dir = os.path.join(test_dir, 'fall')
# os.mkdir(test_fall_dir)

# Directory with our validation notfall pictures
test_notfall_dir = os.path.join(test_dir, 'notfall')
# os.mkdir(test_notfall_dir)

'''
# Copy first 1000 fall images to train_fall_dir
fnames = ['fall.{}.jpg'.format(i) for i in range(556)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/fall", fname)
    dst = os.path.join(train_fall_dir, fname)
#     print(src)
    shutil.copyfile(src, dst)

# Copy next 500 fall images to validation_fall_dir
fnames = ['fall.{}.jpg'.format(i) for i in range(556, 834)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/fall", fname)
    dst = os.path.join(validation_fall_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy next 500 fall images to test_fall_dir
fnames = ['fall.{}.jpg'.format(i) for i in range(834, 948)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/fall", fname)
    dst = os.path.join(test_fall_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy first 1000 notfall images to train_notfall_dir
fnames = ['notfall.{}.jpg'.format(i) for i in range(742)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/notfall", fname)
    dst = os.path.join(train_notfall_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy next 500 notfall images to validation_notfall_dir
fnames = ['notfall.{}.jpg'.format(i) for i in range(742, 1113)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/notfall", fname)
    dst = os.path.join(validation_notfall_dir, fname)
    shutil.copyfile(src, dst)
    
# Copy next 500 notfall images to test_notfall_dir
fnames = ['notfall.{}.jpg'.format(i) for i in range(1113, 1484)]
for fname in fnames:
    src = os.path.join(original_dataset_dir+"/notfall", fname)
    dst = os.path.join(test_notfall_dir, fname)
    shutil.copyfile(src, dst)


print('total training fall images:', len(os.listdir(train_fall_dir)))
print('total training notfall images:', len(os.listdir(train_notfall_dir)))
print('total validation fall images:', len(os.listdir(validation_fall_dir)))
print('total validation notfall images:', len(os.listdir(validation_notfall_dir)))
print('total test fall images:', len(os.listdir(test_fall_dir)))
print('total test notfall images:', len(os.listdir(test_notfall_dir)))
'''

# CNN model

model = models.Sequential()
model.add(layers.Conv2D(64, (3, 3), activation='relu',
                        input_shape=(200, 200, 3)))
model.add(layers.Conv2D(64, (3, 3), activation='relu',padding='same'))
# model.add(layers.Conv2D(64, (3, 3), activation='relu',padding='same'))
# model.add(layers.Dropout(0.1))
model.add(BatchNormalization())
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='relu',padding='same'))
# model.add(layers.Conv2D(128, (3, 3), activation='relu',padding='same'))
# model.add(layers.Conv2D(128, (3, 3), activation='relu',padding='same'))
model.add(layers.Dropout(0.1))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(256, (3, 3), activation='relu',padding='same'))
# model.add(layers.Conv2D(256, (3, 3), activation='relu',padding='same'))
model.add(layers.Dropout(0.1))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(512, (3, 3), activation='relu',padding='same'))
# model.add(layers.Conv2D(512, (3, 3), activation='relu',padding='same'))
model.add(layers.Dropout(0.2))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(128, activation='relu'))
# model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))


model.compile(loss='binary_crossentropy',
              optimizer=optimizers.Adam(lr=1e-4),
              metrics=['acc'])


# train
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)
# train_datagen = ImageDataGenerator(rescale=1./255)

# Note that the validation data should not be augmented!
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        train_dir,
        # All images will be resized to 150x150
        target_size=(200, 200),
        batch_size=20,
        # Since we use binary_crossentropy loss, we need binary labels
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        validation_dir,
        target_size=(200, 200),
        batch_size=20,
        class_mode='binary')

for data_batch, labels_batch in train_generator:
    print('data batch shape:', data_batch.shape)
    print('labels batch shape:', labels_batch.shape)
    break

history = model.fit_generator(
      train_generator,
      steps_per_epoch=int(1298/20),
      epochs=30,
      validation_data=validation_generator,
      validation_steps=10)

#  model save
model.save('falldown/saved_model/my_model')