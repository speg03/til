import argparse


def sub1():
    print('Run sub1 function')


def sub2():
    print('Run sub2 function')


def main():
    # サブコマンドで共通の引数を定義
    # helpオプションはサブコマンド側とconflictするので無効にしておく
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument('--param1')

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    sub1_parser = subparsers.add_parser('sub1', parents=[common])
    sub1_parser.add_argument('--param2')
    sub1_parser.set_defaults(func=sub1)

    sub2_parser = subparsers.add_parser('sub2', parents=[common])
    sub2_parser.set_defaults(func=sub2)

    args = parser.parse_args()
    print(args)

    args.func()


if __name__ == '__main__':
    main()
