import re

def correct_dates(string):
    return re.sub(r'(\d+)/(\d+)/(\d)', r'\2/\1/\3', string)
    # \d is voor digit 

datum = '2/1/2000'

print('Orginele datum:')
print(datum)

print('Aangepaste datum:')
aangepast = correct_dates(datum)
print(aangepast)