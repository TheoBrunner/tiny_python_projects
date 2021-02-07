#!/usr/bin/env python
"""
Author: Theo Brunner
Purpose: Say hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to great')
    return parser.parse_args()


def main():
    """Main programm"""
    args = get_args()
    print('Hello, ' + args.name + '!')


if __name__ == '__main__':
    main()
