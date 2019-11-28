import keras
from keras import layers



from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'D:/天池/train',
    target_size=(78, 78),
    batch_size=40
)

test_generator = test_datagen.flow_from_directory(
    'D:/天池/valid',
    target_size=(78, 78),
    batch_size=40
)

covn_base = keras.applications.VGG16(weights='imagenet', include_top=False)

model = keras.Sequential()
model.add(covn_base)
model.add(layers.GlobalAveragePooling2D())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(10, activation='softmax'))

covn_base.trainable = False

model.summary()

model.compile(optimizer=keras.optimizers.Adam(lr=0.001),
              loss='categorical_crossentropy',
              metrics=['acc'])

history = model.fit_generator(
    train_generator,
    # steps_per_epoch=10,
    epochs=15,
    # validation_data=test_generator,
    # validation_steps=10
)

model.evaluate_generator(generator=test_datagen)

