from random import randint
from math import sqrt

def  make_vec():
  x = randint(-10, 10)
  y = randint(-10, 10)
  z = randint(-10, 10)
  return [x, y, z]

def vector_print(vektor, navn):
  print(f'{navn} = {vektor}')

def scalar_mult(vektor, num):
  nyVektor = []
  for verdi in vektor:
    nyVerdi = verdi * num
    nyVektor.append(nyVerdi)
  return nyVektor

def vec_len(vektor):
  sum = 0
  for verdi in vektor:
    nyVerdi = verdi ** 2
    sum += nyVerdi
  return sqrt(sum)

def vector_dot_product(vektor1, vektor2):
  nyVektor = []
  for i in range(len(vektor1)):
    nyVerdi = vektor1[i] * vektor2[i]
    nyVektor.append(nyVerdi)
  return nyVektor

def main():
  vektor1 = make_vec()
  vector_print(vektor1, 'vec1')

  skalar = float(input('Skriv inn en skalar: '))
  skalertVektor = scalar_mult(vektor1, skalar)

  vektor1Lengde = vec_len(vektor1)
  skaletVektorLengde = vec_len(skalertVektor)

  print(f'Lengden før skalering er: {format(vektor1Lengde, ".2f")}')
  print(f'Lengden etter skalering er: {format(skaletVektorLengde, ".2f")}')
  print(f'Forholdet mellom lengden før og etter skalering er: {skaletVektorLengde/vektor1Lengde}')

  print(f'Prikkproduktet av {vektor1} og {skalertVektor} er: {vector_dot_product(vektor1, skalertVektor)}')

main()