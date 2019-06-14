import pandas as pd
from tensorflow.keras import layers, optimizers, Sequential, utils

data = pd.read_csv("captcha/learn2.csv", header=None)

X_train = data.iloc[:, :-1] / 255.0
Y_train = data.iloc[:, -1]

X_train = X_train.values.reshape(-1, 21, 12, 1)
Y_train = utils.to_categorical(Y_train)

model = Sequential((
    layers.Conv2D(32, kernel_size=(5, 5), padding="same", activation='relu', input_shape=(21, 12, 1)),
    layers.Conv2D(32, kernel_size=(5, 5), padding="same", activation='relu'),
    layers.MaxPool2D(pool_size=(2, 2)),
    layers.Dropout(0.25),

    layers.Conv2D(64, kernel_size=(3, 3), padding="same", activation='relu'),
    layers.Conv2D(64, kernel_size=(3, 3), padding="same", activation='relu'),
    layers.MaxPool2D(pool_size=(2, 2), strides=(2, 2)),
    layers.Dropout(0.25),

    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.25),
    layers.Dense(35, activation='softmax'),
))

optimizer = optimizers.RMSprop(lr=1e-3)
model.compile(optimizer=optimizer, loss="categorical_crossentropy", metrics=['accuracy'])

epochs = 40
model.fit(X_train, Y_train, epochs=epochs, validation_data=None)
model.save('captcha_model.ckpt')
