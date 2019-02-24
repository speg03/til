#!/usr/bin/env python

import argparse
import os

import numpy as np
import tensorflow.keras.backend as K
from tensorflow.keras.layers import (Activation, Conv2D, Dense, Dropout,
                                     Flatten, MaxPooling2D)
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical


def parse_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--input', default='/opt/ml/input/data/training/cifar10.npz')
    parser.add_argument('--model_dir', default='/opt/ml/model')

    parser.add_argument('--batch_size', type=int, default=32)
    parser.add_argument('--epochs', type=int, default=10)
    parser.add_argument('--loss', default='categorical_crossentropy')
    parser.add_argument('--optimizer', default='adam')

    parser.add_argument('--limit_data_rate', type=float, default=1.0)
    parser.add_argument('-v', '--verbose', action='store_true')

    return parser.parse_args()


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(path)

    with np.load(path) as f:
        x_train = f['x_train']
        y_train = f['y_train']
        x_test = f['x_test']
        y_test = f['y_test']

    x_train = x_train.astype('f') / 255.0
    x_test = x_test.astype('f') / 255.0

    y_train = to_categorical(y_train, num_classes=10)
    y_test = to_categorical(y_test, num_classes=10)

    return (x_train, y_train), (x_test, y_test)


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


def main():
    args = parse_arguments()

    (x_train, y_train), (x_test, y_test) = load_data(args.input)

    model = build_model()
    model.compile(
        loss=args.loss, optimizer=args.optimizer, metrics=['accuracy'])

    train_length = int(len(x_train) * args.limit_data_rate)
    test_length = int(len(x_test) * args.limit_data_rate)

    model.fit(
        x_train[:train_length],
        y_train[:train_length],
        batch_size=args.batch_size,
        epochs=args.epochs,
        validation_data=(x_test[:test_length], y_test[:test_length]),
        verbose=1 if args.verbose else 2)

    os.makedirs(args.model_dir, exist_ok=True)
    model.save(os.path.join(args.model_dir, 'model.h5'))

    K.clear_session()


if __name__ == '__main__':
    main()