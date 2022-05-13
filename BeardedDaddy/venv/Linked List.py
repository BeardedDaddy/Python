

graph = {
    1:[2, 3, None],
    2:[4, None],
    3:[None],
    4:[5, 6, None],
    5:[6, None],
    6:[None]
}

from collections import deque
deque(['a', 'b', 'c'])
deque('abc')
deque([{'data': 'a'}, {'data': 'b'},])

llist = deque("abcde")

llist.append('f')
llist.pop()
llist.appendleft("z")
llist.popleft()
print(llist)
