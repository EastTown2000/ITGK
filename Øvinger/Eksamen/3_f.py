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

print(get_actual_ev('Nevada', 25, 75))

print(get_actual_ev_fair("Nevada", 50.1, 49.9))
print(get_actual_ev_fair("Georgia", 80, 20))