#!/usr/bin/env python3

# based on: https://www.tensorflow.org/guide/keras

import argparse
import os

import numpy as np
import tensorflow as tf
from tensorflow.keras import layers


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--learning_rate", type=float, default=1e-3)
    parser.add_argument("--checkpoint_dir", default="checkpoints")
    parser.add_argument("--model_dir")

    return parser.parse_args()


def generate_model():
    model = tf.keras.Sequential()
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(10, activation="softmax"))

    return model


def generate_data(n, n_feature, n_class):
    data = np.random.random((n, n_feature))

    classes = np.random.randint(0, n_class, n)
    labels = np.zeros((n, n_class))
    labels[np.arange(n), classes] = 1

    return data, labels


def main():
    args = parse_arguments()

    model = generate_model()
    model.compile(
        optimizer=tf.keras.optimizers.Adam(lr=args.learning_rate),
        loss="categorical_crossentropy",
        metrics=["accuracy"],
    )
    data, labels = generate_data(1000, 32, 10)

    os.makedirs(args.checkpoint_dir, exist_ok=True)
    checkpoint_path = os.path.join(args.checkpoint_dir, "model.h5")
    callbacks = [tf.keras.callbacks.ModelCheckpoint(checkpoint_path)]

    model.fit(
        data,
        labels,
        epochs=args.epochs,
        batch_size=args.batch_size,
        callbacks=callbacks,
        verbose=2,
    )


if __name__ == "__main__":
    main()
