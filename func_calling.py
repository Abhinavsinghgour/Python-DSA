

import sys


def main():
    x=input('Name please :')
    hello(x)
    goodbye(x)

def hello(x):
    print(f'hello {sys.argv[1]}')

def goodbye(x):
    print(f'goodbye {sys.argv[2]}')                


if __name__ == "__main__":
    main()

       ==========================================================================================================

import sys
from tryyy import hello


if len(sys.argv)==2:
    hello(sys.argv[1])

