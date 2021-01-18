
# NB: eksemplene i disse filene er inne nødvendigvis
# fullstendige. Les oppgavene i Inspera for å få krav-
# spesifikasjonen!

# Du må erstatte 'funksjonsnavn' med det som faktisk spørres etter, da!

'''
Oppgave 3.1: calculate_percentage
'''
# Prosentforhold mellom de to (returnerer tuppel med to varible)
# def funksjonsnavn:

# Disse linjene kan brukes for å sjekke koden din:
#print(f'Dette skal bli (33.49, 66.51): {calculate_percentage((139, 276))}.')



'''
Oppgave 3.2: return_total_votes
'''

# def funksjonsnavn:

# Disse linjene kan brukes for å sjekke koden din:
# nevada_votes = [(16, 60), (87, 127), (36, 89)]
# print(f"Totale stemmer i Nevada skal være (139, 276): {return_total_votes(nevada_votes)}")



'''
Oppgave 3.3: update_state

'''
# def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din:
# votes = {'Pennsylvania': [(55, 106), (68, 103)], \
# 'Nevada': [(16, 60), (87, 127)]} 
# votes = update_state(votes, 'Nevada', 36, 89)
# print(f"This should print [(16, 60), (87, 127), (36, 89)]: {votes['Nevada']}.")



'''
Oppgave 3.4: read_from_file
'''

#def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din, votes brukes også senere!
# votes = read_from_file() 
# print(votes)


# Denne må med til de resterende oppgavene:
electoral_votes = [["Arizona", 11], ["Nevada", 6], ["Pennsylvania", 20], ["Georgia", 16]]


'''
Oppgave 3.5: get_ev_for_state
'''

#def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din:
# print(f"Electoral votes for Nevada should be 6: {get_ev_for_state('Nevada')}.")


'''
Oppgave 3.6: get_actual_ev
'''

#def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din:
# vote_tuple = return_total_votes(votes['Nevada'])
# dem_perc, rep_perc = calculate_percentage(votes_tuple)
# nevada = get_actual_ev("Nevada", dem_perc, rep_perc)
# print(f"I Nevada skal republikanerne vinne: {nevada}.")


'''
Oppgave 3.7: get_actual_ev_fair
'''

#def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din:
# fair = get_actual_ev_fair("Nevada", 49.9, 50.1)
# print(f"Hvis vi fordeler etter prosent skal begge få 3: {fair}.")


'''
Oppgave 3.8: print_nation_results
'''

#def funksjonsnavn

# Disse linjene kan brukes for å sjekke koden din:
# print_nation_results(votes)
