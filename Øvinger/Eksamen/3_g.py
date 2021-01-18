def calculate_percentage(tpl):
  a = tpl[0]
  b = tpl[1]
  c = a + b
  a_p = round(a/c*100,2)
  b_p = round(b/c*100,2)
  return (a_p, b_p)

def return_total_votes(lst):
  dem = 0
  rep = 0
  for votes in lst:
    dem = dem + votes[0]
    rep = rep + votes[1]
  return(dem,rep)

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

electoral_votes = [["Arizona", 11], ["Nevada", 6], ["Pennsylvania", 20], ["Georgia", 16]]
def get_ev_for_state(state):
  for states in electoral_votes:
    if states[0] == state:
      return states[1]

def get_actual_ev(state, dempercent, reppercent):
  ev = get_ev_for_state(state)
  if dempercent < reppercent:
    return (0, ev)
  else:
    return (ev, 0)

def get_actual_ev_fair(state, dempercent, reppercent):
  ev = get_ev_for_state(state)
  dem_float = dempercent/100
  rep_float = reppercent/100
  dem_ev = round(ev*dem_float)
  rep_ev = round(ev*rep_float)
  return (dem_ev, rep_ev)


votes = read_from_file()

def print_nation_results(votes):  
  def get_state_votes():
    states = ["Arizona", "Nevada", "Pennsylvania", "Georgia"]
    state_votes = []
    for state in states:
      s_votes = return_total_votes(votes[state])
      state_votes.append([state, s_votes])
    return state_votes
  
  state_votes = get_state_votes()
  
  def state_percent(lst):
    state_percent = []
    for state in lst:
      tpl = state[1]
      percent = calculate_percentage(tpl)
      state_percent.append([state, percent])
    return state_percent
  
  state_percent = state_percent(state_votes)
  
  ev = get_actual_ev(state_percent[0], state_percent[1][0], state_percent[1][1])
  
  ev_fair = get_actual_ev_fair(state_percent[0], state_percent[1][0], state_percent[1][1])
  
  def vote_total(lst):
    vote_tpl = []
    for state in lst:
      vote_tpl.append(state[1])
    total = return_total_votes(vote_tpl)
    return total
  
  total = vote_total(state_votes)
  
  print(f'Dems got {total[0]} votes, reps got {total[1]}.\n'
        f'With wta, dems got {ev[0]} while reps got {ev[1]} electoral votes\n'
        f'With fair, dems got {ev_fair[0]} while reps got {ev_fair[1]} electoral votes')

print_nation_results(votes)
