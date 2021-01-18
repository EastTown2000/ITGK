def update_state(dict, state, demvotes, repvotes):
    if state in dict:
        dict[state].append((demvotes, repvotes))
    else:
        dict[state] = [(demvotes, repvotes)]
    return dict

def read_from_file():
  vote_file = open('votes.txt', 'r')
  votes = vote_file.read()
  votes = votes.split('\n')
  dict = {}
  for statevotes in votes:
    votes_split = statevotes.split(',')
    try:
      update_state(dict, votes_split[0], int(votes_split[1]), int(votes_split[2]))
    except Exception:
      print(f'Linje kunne ikke tolkes: {statevotes}')
  vote_file.close()
  return dict  

votes = read_from_file()
print(votes)