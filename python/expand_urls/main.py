#!/usr/bin/env python

import argparse
from urllib.error import HTTPError
from urllib.request import Request, urlopen


def expand_url(url):
    req = Request(url, method='HEAD')

    try:
        url = urlopen(req).url
    except HTTPError as e:
        url = e.url

    return url


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url')
    args = parser.parse_args()

    print(expand_url(args.url))


if __name__ == '__main__':
    main()
