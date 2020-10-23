def lastTwo(liste):
    return ''.join([str[-2:] for str in liste])

liste = ["banan","propan","Westerosi"]
print(lastTwo(liste))