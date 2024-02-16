"""
This line of code initializes a variable named
'Text' with a string value
"what have the romans ever done for us".
The 'Text' variable can be used later in the code
for various operations such as string manipulation, printing, etc.
"""
TEXT = "what have the romans ever done for us"

capitals = [char.upper() for char in TEXT]

print(capitals)

words = [word.upper() for word in TEXT.split(' ')]
print(words)

lc_words = TEXT.split(' ')
print(lc_words)
