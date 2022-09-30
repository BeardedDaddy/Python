""" This module explains how to strip words from a line in a parograph."""
def removeprefix(string: str, prefix: str) -> str:
    """ This function removes the first word at the beginning of the line."""
    if string.startswith(prefix):
        return string[len(prefix):]
    else:
        return string[:] # Return a copy of 'string'.
def removesuffix(string: str, suffix: str) -> str:
    """ This function removes the last word at the end of the line"""
    if suffix and string.endswith(suffix): # suffix = '' should not call string[:-0]
        return string[:-len(suffix)]
    else:
        return string [:]

FILENAME = 'Jabberwocky.txt'
with open(FILENAME, encoding='utf-8') as poem:
    first = poem.readline().rstrip()

print(first)
# In this next block of code strips the apostrophe from the first character of the string.
#CHARS = "'"
# # In this line strips the apostrophe from the first character of the string.
#CHARS = "'Twas"
# CHARS = "'Twas" # In this line strips everything in the double quotes. That's why it has removed the s at the end of 'toves'.
#CHARS = "'Twasebv"
# In this line of code the .strip method removes all the characters in the double quotes until .strip reaches a characters that is not in CHARS.
CHARS = "'Twase bv"
# In this line of code the .strip method removes all the characters on the right hand side until it finds something that we didn't include.
# no_apostrophe = first.strip(CHARS)
# print(no_apostrophe)

for character in first:
    if character in CHARS:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80)

for character in first[::-1]: # process backwards
    if character in CHARS:
        print(f'removing "{character}"')
    else:
        break

print('*' * 80) 

# twas_removed = first.removeprefix("'Twas")
twas_removed = removeprefix(first, "'Twas")
print(twas_removed)
# toves_removed = first.removesuffix('toves')
toves_removed = removesuffix(first, "toves")
print(toves_removed)
