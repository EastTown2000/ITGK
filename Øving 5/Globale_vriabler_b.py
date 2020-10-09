from math import sqrt
GRAVITY = 9.81

def get_fall_time(m, gravity=GRAVITY):
    t = sqrt(2 * m / gravity)
    return t

#Måten i eksempelet fungerer, men det er letter å gjøre som over