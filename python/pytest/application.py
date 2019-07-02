import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name")
    args = parser.parse_args()

    template = sys.stdin.read()
    print(template.format(args.name))


if __name__ == "__main__":
    main()
