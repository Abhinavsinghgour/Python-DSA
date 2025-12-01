#Modules in Py

# random
# -----random.choice(seq)
# -----random.randint(a,b)
#------random.sniff



from random import choice
x = 'head'
while (x == 'head'):
    x= choice(['head', 'tails'])
    print(x)

from random import randint
num=randint(1,10)
print(num)

from random import shuffle
cards= ["A","B","C","D","E","F"]
shuffle(cards)
for card in cards:
    print(card)
