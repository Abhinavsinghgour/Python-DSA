# Methodology of calling function from one file to another

# File No.01

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
# File No.02
import sys
from tryyy import hello


if len(sys.argv)==2:
    hello(sys.argv[1])

