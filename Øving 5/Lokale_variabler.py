#a)
    #1)
        #Man må definere en variabel før man bruker den, her er ikke cake definert
    #2)
        #Man må definere en variabel før man bruker den, her er ikke cupcake definert, fordi det ikke er en global variabel
    #3)
        #Her er ikke cake definert, og funksjonen cakes blir ikke kjørt

#b)
    def Heltallsdivisjon(x, y):
        num = x // y
        return num

    def Kvadrat(x):
        num = x**2
        return num

    a = 23
    b = 4
    print(f'Heltallsdivisjon av {a} over {b} gir {Heltallsdivisjon(a, b)}')

    c = 3
    print(f'Kvadratet av {c} er {Kvadrat(c)}')

#c)
#Det gir ikke problemer her fordi num er en lokal variabel i de to funksjonene, 
#num kommer aldri ur av funksjonen fordi det som kommer ut har navner funksjon(variabel) ikke num