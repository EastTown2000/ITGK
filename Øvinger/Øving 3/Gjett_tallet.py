from random import randint

nedre = int(input('Gi en nedre grense for det tilfeldige tallet: '))
oevre = int(input('Gi en øvre grense for det tilfeldige tallet: '))
tall = randint(nedre, oevre)

def guess(g_num):
    if g_num == tall:
        print('You guessed correct!')
        exit(0)
    elif g_num < tall:
        print('The correct Number is higher')
    else:
        print('The correct number is lower')

while True:
    gjett = int(input('Make a guess '))
    
    guess(gjett)
    