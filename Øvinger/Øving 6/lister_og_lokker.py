number_list = []
for i in range(100):
  number_list.append(i)
print(number_list)

nummerSum = 0
for nummer in number_list:
  if nummer % 3 == 0 or nummer % 10 == 0:
    nummerSum += nummer
print(nummerSum)

for nummer in range(0, len(number_list), 2):
  partall = number_list[nummer]
  oddetall = number_list[nummer+1]
  number_list[nummer] = oddetall
  number_list[nummer + 1] = partall
print(number_list)

nyListe = []
for nummer in range(len(number_list)):
  indeks = len(number_list) - 1 - nummer
  nyListe.append(number_list[indeks])
print(nyListe)