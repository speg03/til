import numpy as np
from tensorflow.keras.datasets import cifar10


def main():
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    np.savez(
        './cifar10.npz',
        x_train=x_train,
        y_train=y_train,
        x_test=x_test,
        y_test=y_test)


if __name__ == '__main__':
    main()
