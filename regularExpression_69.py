import re

pattern = r"[a-z]+loom"

text = '''In the garden, flowers bloom,
Exuding scents that banish gloom.
Colors blend in a vibrant dance,
Nature's artwork, a joyful chance.'''

# only search the first occurence
# match = re.search(pattern, text)

# search all the occurence
matches = re.finditer(pattern, text)

for match in matches:
    print(match)
    print(match.span())
    print(text[match.span()[0]: match.span()[1]])