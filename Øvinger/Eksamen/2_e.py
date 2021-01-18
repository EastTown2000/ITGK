a =  [['Beatles','And I love her'],['Beatles','All my loving'], ['Traffic','John Barleycorn must die'],['Cream','Sunshine of my love'],['Cream','SLWABR']]
def list_to_disc(lst, name):
  txt = open(name, 'w')
  for song in lst:
    txt.write(f'{song[0]};{song[1]}\n')
  txt.close()

list_to_disc(a, 'song.txt')