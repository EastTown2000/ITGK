def calculate_percentage(tpl):
  a = tpl[0]
  b = tpl[1]
  c = a + b
  a_p = round(a/c*100,2)
  b_p = round(b/c*100,2)
  return (a_p, b_p)

print(f'Dette skal bli (33.49, 66.51): {calculate_percentage((139, 276))}.')