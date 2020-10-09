from math import sqrt
GRAVITY = 9.81

def get_fall_time(m):
    t = sqrt(2 * m / GRAVITY)
    return t


distanse = int(input('Hvor langt skal objektet falle: '))
print(f'Da tar det {get_fall_time(distanse)} sekunder')