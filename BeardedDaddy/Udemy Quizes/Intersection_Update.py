text = """Education is not the learning of facts but the training of the mind to think"""

prepositions = {'as', 'but', 'by', 'down',
                'for', 'in', 'of', 'on', 'to', 'with'}

words = text.split()

preps_used = prepositions.intersection(words)
print(preps_used)
