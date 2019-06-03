import argparse


class NestedNamespace(argparse.Namespace):
    DELIMITER = '.'

    def __setattr__(self, name, value):
        try:
            namespace, name = name.split(self.DELIMITER, maxsplit=1)
        except ValueError:
            namespace = None

        if namespace:
            if not hasattr(self, namespace):
                super().__setattr__(namespace, NestedNamespace())
            setattr(getattr(self, namespace), name, value)
        elif namespace is not None:
            setattr(self, name, value)
        else:
            super().__setattr__(name, value)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo.bar.param1', default=1)
    parser.add_argument('--foo.bar.param2', default=2)

    args = parser.parse_args(namespace=NestedNamespace())
    print(args)


if __name__ == '__main__':
    main()
