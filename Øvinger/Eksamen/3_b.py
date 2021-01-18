def return_total_votes(lst):
  dem = 0
  rep = 0
  for votes in lst:
    dem = dem + votes[0]
    rep = rep + votes[1]
  return(dem,rep)

nevada_votes = [(16, 60), (87, 127), (36, 89)]

print(return_total_votes(nevada_votes))
