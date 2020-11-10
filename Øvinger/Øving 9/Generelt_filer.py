#a)
def write_to_file(data):
    f = open('my_file.txt', 'w')
    f.write(data)
    f.close()

#b)    
def read_from_file(filname):
    f = open(filname,'r')
    contens = f.read()
    print(contens)
    f.close()


#c)
def main():    
    a = input('Do you want to read or write to my_file? ')
    while True:
        if a == 'write':
            write_to_file(input('What do you want to write to the file? '))
        elif a == 'read':
            read_from_file('my_file.txt')
        elif a == 'done':
            break
        else:
            print('You did not put in a valid comand try again')
        print('If you are done say "done"')
        a = input('Do you want to read or write to my_file? ')
        

main()   
            