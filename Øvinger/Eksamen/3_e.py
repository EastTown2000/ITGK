electoral_votes = [["Arizona", 11], ["Nevada", 6], ["Pennsylvania", 20], ["Georgia", 16]]
def get_ev_for_state(state):
  for states in electoral_votes:
    if states[0] == state:
      return states[1]

print(get_ev_for_state('Nevada'))