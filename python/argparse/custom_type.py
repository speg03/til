import argparse
import re

import numpy as np


def shape(string):
    m = re.search(r'^\s*\(([\d\s,]+)\)\s*$', string)
    if m is None:
        raise ValueError
    return tuple(map(int, m.group(1).split(',')))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-shape', type=shape)
    args = parser.parse_args()

    print(np.ones(args.input_shape))


if __name__ == '__main__':
    main()
