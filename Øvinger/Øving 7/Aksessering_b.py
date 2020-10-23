def third_letter(string):
    try:
        return string[2]
    except IndexError:
        return 'q'

print(third_letter("Temeria")) #skal gi "m"
print(third_letter("IT")) #skal printe ut "q"