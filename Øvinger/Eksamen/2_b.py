
def prepare(x):
  length = len(x)
  for num in x:
    if num == '0' or num == '1':
      continue
    else:
      return 'Dette er ikke et binært tall'  
  if length % 3 == 0:
    added0 = 0
  elif length % 3 == 1:
    added0 = 2
  elif length % 3 == 2:
    added0 = 1
  return added0*'0'+ x
