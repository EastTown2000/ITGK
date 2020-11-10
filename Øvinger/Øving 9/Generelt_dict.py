#a)
my_family = dict()

#b/c)
def add_family_member(role, name):
    if role in my_family:
        my_family[role].append(name)
    else:
        my_family[role] = [name]

add_family_member('bror', 'Ole')
add_family_member('bror', 'Arne')
add_family_member('mor', 'Anne')
add_family_member('bror', 'Geir')

#d)
for key in my_family: print(key, my_family[key])