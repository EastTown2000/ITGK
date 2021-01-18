def convert(x):
  if len(x) > 5:
    x = x[-5: -1]
  new_char = 0
  for char in x:
    new_char = new_char + ord(char)
  return chr(new_char)

print(convert('abc'))