#!/usr/bin/env python

import argparse
import os

import numpy as np
import tensorflow.keras.backend as K
from tensorflow.keras.layers import (Activation, Conv2D, Dense, Dropout,
                                     Flatten, MaxPooling2D)
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import SGD, Adagrad, Adam, RMSprop
from tensorflow.keras.utils import to_categorical


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('--model_dir')
    parser.add_argument(
        '--train_dir',
        default=os.getenv('SM_CHANNEL_TRAIN', './data/cifar10/train'))
    parser.add_argument('--train_file', default='cifar10_train.npz')
    parser.add_argument(
        '--val_dir',
        default=os.getenv('SM_CHANNEL_VALIDATION', './data/cifar10/val'))
    parser.add_argument('--val_file', default='cifar10_val.npz')
    parser.add_argument(
        '--save_model_dir', default=os.getenv('SM_MODEL_DIR', './model'))

    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--optimizer', default='adam')
    parser.add_argument('--learning_rate', type=float, default=0.001)

    parser.add_argument('--limit_data_rate', type=float, default=1.0)
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    with np.load(path) as f:
        x = f['x']
        y = f['y']

    x = x.astype('f') / 255
    y = to_categorical(y, num_classes=10)

    return x, y


def build_model(input_shape=(32, 32, 3), num_classes=10):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), padding='same', input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(num_classes))
    model.add(Activation('softmax'))

    return model


def build_optimizer(name, learning_rate=0.01):
    if name.lower() == 'sgd':
        optimizer = SGD(lr=learning_rate)
    elif name.lower() == 'adagrad':
        optimizer = Adagrad(lr=learning_rate)
    elif name.lower() == 'rmsprop':
        optimizer = RMSprop(lr=learning_rate)
    elif name.lower() == 'adam':
        optimizer = Adam(lr=learning_rate)
    else:
        raise ValueError(f'Unknown optimizer: {name}')

    return optimizer


def main():
    args = parse_arguments()
    print(f'Arguments: {args}')

    x_train, y_train = load_data(os.path.join(args.train_dir, args.train_file))
    x_test, y_test = load_data(os.path.join(args.val_dir, args.val_file))

    model = build_model()
    model.compile(
        loss='categorical_crossentropy',
        optimizer=build_optimizer(args.optimizer, args.learning_rate),
        metrics=['accuracy'])

    train_length = int(len(x_train) * args.limit_data_rate)
    test_length = int(len(x_test) * args.limit_data_rate)

    model.fit(
        x_train[:train_length],
        y_train[:train_length],
        batch_size=args.batch_size,
        epochs=args.epochs,
        validation_data=(x_test[:test_length], y_test[:test_length]),
        verbose=1 if args.verbose else 2)

    os.makedirs(args.save_model_dir, exist_ok=True)
    model.save(os.path.join(args.save_model_dir, 'model.h5'))

    K.clear_session()


if __name__ == '__main__':
    main()
