# command line argument : means writing 'custom' argument in terminal at runtime
# sys.argv[0] : save program name Ex. python try.py abhi here try.py is pra
# sys.exit() : exit system at that point

import sys
if len(sys.argv) <2:
    sys.exit("Too short")
elif len(sys.argv)>2:
    sys.exit('Too long')

print('hello',sys.argv[1])
