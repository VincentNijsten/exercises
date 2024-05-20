import re
def remove_repeated_words(string):
    return re.sub(r'(\b[a-zA-Z]+\b)( \1)+', r'\1', string)
    # we zoeken een woord dat a-z of A-Z heeft en twee keer na elkaar voor komt, vandaar de ( \1)

# Voorbeeld string met herhaalde woorden
example_string = "Dit is is een voorbeeld voorbeeld van van een een herhaalde herhaalde zin zin."
print("Originele string:")
print(example_string)

# Roep de functie aan en druk het resultaat af
cleaned_string = remove_repeated_words(example_string)

print("\nString zonder herhaalde woorden:")
print(cleaned_string)