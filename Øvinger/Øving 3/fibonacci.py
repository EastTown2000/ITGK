def fibonacci(etterspurt): 
    """
    gir en liste(int) av fibonacci-nummerene
    """
    f_0 = 0
    f_1 = 1
    i = 1
    result = []
    while (i <= etterspurt):
        result.append(f_0)
        tidf_1 = f_1
        f_1 = f_1 + f_0
        f_0 = tidf_1
        i += 1
    return result


fnum = int(input('Skriv nummeret på fibonacci tallet du vil ha: '))

a = fibonacci(fnum)

print()
print('a)')
print(f'Fibonacci tall {fnum} er {a[-1]},')
print('b)')
print(f'Og summen av fibonaccitallene opp til {fnum} er {sum(a)}')
print('c)')
print(f'De første {fnum} fibonaccinummerene er {a}')