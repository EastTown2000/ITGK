def update_state(dict, state, demvotes, repvotes):
    if state in dict:
        dict[state].append((demvotes, repvotes))
    else:
        dict[state] = [(demvotes, repvotes)]
    return dict


votes = {'Pennsylvania': [(55, 106), (68, 103)], \
'Nevada': [(16, 60), (87, 127)]} 
votes = update_state(votes, 'bama', 36, 89)
print(votes['bama'])