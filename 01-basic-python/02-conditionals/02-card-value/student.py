def card_value(string):
    if string == 'Ace':
        return 1
    elif string == 'King':
        return 13
    elif string == 'Queen':
        return 12
    elif string == 'Jack':
        return 11
    elif 2 <= int(string) <= 10:
        return string
    else:
        return 'Kaart bestaat ni'
print(card_value('15'))