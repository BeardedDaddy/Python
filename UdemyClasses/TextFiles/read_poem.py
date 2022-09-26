"""This is the process on how to open a text file."""
# jabber = open('Jabberwocky.txt', 'r', encoding='utf-8')

# for line in jabber:
#     print(line.rstrip())
#     # print(len(line))

# jabber.close()

# with open('Jabberwocky.txt', 'r', encoding='utf-8') as jabber:
#     #     for line in jabber:
#     #         print(line.rstrip())
#     lines = jabber.readlines()

# print(lines)
# print(lines[-1:])
# for line in reversed(lines):
#     print(line, end='') # Processing this poem in reverse

with open('Jabberwocky.txt', 'r', encoding='utf-8') as jabber:
    text = jabber.read()

print(text)
