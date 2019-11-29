#!/usr/bin/env python3

import sys
import os


ENVS_PATH = os.path.expanduser('~/envs')


def main():
    if len(sys.argv) <= 1:
        print('Usage: envman [create <name> | load <name> | show <name>]')
        sys.exit()

    if sys.argv[1] == 'create':
        if not os.path.exists('.env'):
            print('Error: No .env file found in current directory')
            sys.exit()

        if len(sys.argv) < 3:
            print('Error: Please specify a name for the saved .env file')
            sys.exit()

        name = sys.argv[2]
        with open('.env', 'r') as src:
            with open('{}/{}.env'.format(ENVS_PATH, name), 'w') as dest:
                dest.write(src.read())
                print('Saved .env to ~/envs/{}.env'.format(name))

    elif sys.argv[1] == 'load':
        if len(sys.argv) < 3:
            print('Error: Please specify a name for the .env file to load')
            sys.exit()

        name = sys.argv[2]
        if not os.path.exists('{}/{}.env'.format(ENVS_PATH, name)):
            print('Error: Could not find ~/envs/{}.env'.format(name))
            sys.exit()

        with open('{}/{}.env'.format(ENVS_PATH, name), 'r') as src:
            with open('.env', 'w') as dest:
                dest.write(src.read())
                print('Loaded .env from ~/envs/{}.env'.format(name))

    elif sys.argv[1] == 'show':
        if len(sys.argv) < 3:
            print('Error: Please specify a name for the .env file to show')

        name = sys.argv[2]
        if not os.path.exists('{}/{}.env'.format(ENVS_PATH, name)):
            print('Error: Could not find ~/envs/{}.env'.format(name))
            sys.exit()

        with open('{}/{}.env'.format(ENVS_PATH, name), 'r') as src:
            out = src.read()
            print(out)

    else:
        print('Usage: envman [create <name> | load <name> | show <name>]')
        sys.exit()

if __name__ == '__main__':
    main()
