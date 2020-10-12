def propaganda(studenter, emner):
    for nr_student in range(1, studenter + 1):
        for nr_emne in range(1, emner + 1):
            print(f'Stud {nr_student} elsker Emne {nr_emne}', end=' ; ')
        print()

ant_studenter = int(input('Hvor mange studenter? '))
ant_emner = int(input('Hvor mange emner? '))
propaganda(ant_studenter, ant_emner)