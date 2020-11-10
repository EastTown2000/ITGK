#a)
def number_of_lines(filname):
    f = open(filname,'r')
    contens = f.read().split()
    f.close()
    return len(contens)
    
print(number_of_lines('numbers.txt'))

#b/c)
def number_frequency(filname):
    f = open(filname,'r')
    contens = f.read().split()
    f.close()
    a = dict()
    for number in contens:
        b = int(number)
        if b in a:
            a[b] += 1
        else:
            a[b] = 1
    return a

a = number_frequency('numbers.txt')
for key in a: print(f'{key}: {a[key]}')
